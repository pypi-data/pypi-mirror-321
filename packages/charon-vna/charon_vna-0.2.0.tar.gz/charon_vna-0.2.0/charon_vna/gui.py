# %% imports
import json
import pickle
import re
import sys
from pathlib import Path
from typing import List

import matplotlib as mpl
import numpy as np
import skrf as rf
import xarray as xr
from numpy import typing as npt
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import (
    QApplication,
    QDialogButtonBox,
    QFileDialog,
    QInputDialog,
    QLineEdit,
    QMainWindow,
    QMenu,
    QProgressBar,
    QVBoxLayout,
    QWidget,
)
from vna import Charon

from charon_vna.plots import PlotWidget
from charon_vna.util import net2s, s2net

# %%
DEFAULT_CONFIG = Path(__file__).parent / "config_default.json"
CONFIG_SUFFIX = ".json"


class MainWindow(QMainWindow):
    config_path: Path | None
    # device: Charon

    plots: List[PlotWidget]

    def __init__(self, ip: str | None = None):
        super().__init__()

        self.config_path = DEFAULT_CONFIG
        with open(self.config_path, "r") as f:
            config = json.load(f)
        self._frequency = config["frequency"]

        vna_kwargs = dict(
            frequency=self._frequency,
        )
        if ip is not None:
            vna_kwargs["ip"] = ip
        self.vna = Charon(**vna_kwargs)

        mpl.use("QtAgg")

        self.setWindowTitle("Charon VNA")

        # Menu
        menubar = self.menuBar()

        menu_file = QMenu("&File")
        menubar.addMenu(menu_file)
        action_open_config = QAction("&Open Configuration", self)
        menu_file.addAction(action_open_config)
        action_open_config.triggered.connect(self.open_config)
        action_open_config.setShortcut(QKeySequence("Ctrl+O"))
        action_save_config = QAction("&Save Configuration", self)
        menu_file.addAction(action_save_config)
        action_save_config.triggered.connect(self.save_config)
        action_save_config.setShortcut(QKeySequence("Ctrl+S"))
        action_saveas_config = QAction("Save Configuration &As", self)
        menu_file.addAction(action_saveas_config)
        action_saveas_config.triggered.connect(self.saveas_config)
        action_saveas_config.setShortcut(QKeySequence("Ctrl+Shift+S"))

        menu_stimulus = QMenu("&Stimulus")
        menubar.addMenu(menu_stimulus)
        action_set_frequency = QAction("&Frequency", self)
        menu_stimulus.addAction(action_set_frequency)
        action_set_frequency.triggered.connect(self.set_frequency)
        action_set_power = QAction("&Power", self)
        menu_stimulus.addAction(action_set_power)
        # action_set_power.triggered.connect(self.set_power)
        action_trigger = QAction("&Trigger", self)
        action_trigger.triggered.connect(self.capture)
        action_trigger.setShortcut("Ctrl+T")
        menu_stimulus.addAction(action_trigger)

        menu_calibration = QMenu("&Calibration")
        menubar.addMenu(menu_calibration)
        action_cal_solt = QAction("&SOLT", self)
        action_cal_solt.triggered.connect(self.calibrate_solt)
        menu_calibration.addAction(action_cal_solt)

        # Content
        window_layout = QVBoxLayout()

        prog_sweep = QProgressBar()
        prog_sweep.setMinimum(0)
        prog_sweep.setMaximum(100)
        prog_sweep.setFormat("%v / %m")
        # prog_sweep.setTextVisible(False)
        prog_sweep.setValue(50)
        window_layout.addWidget(prog_sweep)
        self.prog_sweep = prog_sweep

        # window_widget.se
        plot_layout = QVBoxLayout()
        # TODO: handle plots properly
        self.plots = []
        for type_ in ["logmag", "phase", "vswr", "smith"]:
            self.plots.append(PlotWidget(type_=type_))
            plot_layout.addWidget(self.plots[-1])
        plot_widget = QWidget()
        plot_widget.setLayout(plot_layout)
        window_layout.addWidget(plot_widget)

        # Set the central widget of the Window.
        widget = QWidget()
        widget.setLayout(window_layout)
        self.setCentralWidget(widget)

    def saveas_config(self) -> None:
        print("Prompting for save path...")
        dialog = QFileDialog(self)
        dialog.setDefaultSuffix(CONFIG_SUFFIX)
        dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
        if dialog.exec():
            config_path = Path(dialog.selectedFiles()[0])
            if config_path.suffix != CONFIG_SUFFIX:
                raise ValueError(
                    f"{config_path.name} is not a valid configuration file. Must have extension {CONFIG_SUFFIX}"
                )
            if config_path == DEFAULT_CONFIG:
                raise ValueError(f"Cannot overwrite default configuration file at {DEFAULT_CONFIG}")
            self.config_path = config_path
            print(f"Config path is now {self.config_path.resolve()}")

            self.save_config()

    def open_config(self) -> None:
        print("Prompting for load path...")
        dialog = QFileDialog(self)
        dialog.setNameFilter(f"*{CONFIG_SUFFIX}")
        dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)
        if dialog.exec():
            config_path = Path(dialog.selectedFiles()[0])
            print(config_path)
            if config_path.suffix != CONFIG_SUFFIX:
                raise ValueError(
                    f"{config_path.name} is not a valid configuration file. Must have extension {CONFIG_SUFFIX}"
                )
            self.config_path = config_path
            print(f"Config path is now {self.config_path.resolve()}")

            self.load_config(self.config_path)

    def save_config(self) -> None:
        if self.config_path == DEFAULT_CONFIG:
            self.saveas_config()
        else:
            print(f"Saving config to {self.config_path.resolve()}")
            # TODO: save config

    def load_config(self, path: Path) -> None:
        print(f"Loading config from {path}...")
        # TODO: load config

    def progress_callback(self, done: int, total: int):
        self.prog_sweep.setMaximum(total)
        self.prog_sweep.setValue(done)

    def capture(self) -> None:
        s = self.vna.vna_capture(self._frequency, self.progress_callback)

        if self.vna.calibration is not None:
            s_calibrated = self.vna.calibration.apply_cal(s2net(s))
            data = net2s(s_calibrated)
        else:
            data = xr.DataArray(
                [[s]],
                dims=["m", "n", "frequency"],
                coords=dict(
                    frequency=s.coords["frequency"],
                    m=[1],
                    n=[1],
                ),
            )

        for plot in self.plots:
            plot.update_plot(data)

    def set_frequency(self, *, frequency: npt.ArrayLike | None = None):
        print(frequency)
        if frequency is None:
            start, ok = QInputDialog.getDouble(
                self, "Start Frequency", "Start Frequency", minValue=30e6, maxValue=6e9, value=1e9
            )
            stop, ok = QInputDialog.getDouble(
                self, "Stop Frequency", "Stop Frequency", minValue=30e6, maxValue=6e9, value=2e9
            )
            points, ok = QInputDialog.getInt(self, "Points", "Points", minValue=2, value=101)
            frequency = np.linspace(start, stop, points)
        # Currently does not support zero span
        self._frequency = frequency

    def calibrate_solt(self):
        if len(self.vna.ports) > 1:
            raise NotImplementedError

        calfile = Path(__file__).parent / "cal.pkl"
        if calfile.exists():
            # don't re-cal while debugging because that's slooooooow
            with open(calfile, "rb") as f:
                calibration = pickle.load(f)
        else:
            s = dict()
            for net in ["short", "open", "load"]:
                input(f"Connect {net} standard and press ENTER...")
                s[net] = self.vna.vna_capture(self._frequency, self.progress_callback)

            ideal = rf.media.DefinedGammaZ0(frequency=rf.media.Frequency.from_f(self._frequency, unit="Hz"))
            calibration = rf.calibration.OnePort(
                [s2net(s["short"]), s2net(s["open"]), s2net(s["load"])],
                [ideal.short(), ideal.open(), ideal.load(0)],
            )
            # TODO: don't use pickles for calibration. They're fragile
            with open(calfile, "wb") as f:
                pickle.dump(calibration, f)
        self.vna.calibration = calibration


def main() -> None:
    app = QApplication(sys.argv)

    try:
        window = MainWindow()
    except Exception as e:
        if e.args[0] == "No device found":
            dialog = QInputDialog()
            text, ok = dialog.getText(
                None,
                "Pluto IP Address",
                "Enter Pluto IP Address",
                QLineEdit.Normal,
                "192.168.2.1",
            )
            match = re.match(r"(\d{1,3}\.){3}\d{1,3}", text)
            if not match:
                raise ValueError(f"Invalid IP address: {text}")
            window = MainWindow(ip=text)
        else:
            raise e

    window.show()

    app.exec()


# %%
if __name__ == "__main__":
    main()
