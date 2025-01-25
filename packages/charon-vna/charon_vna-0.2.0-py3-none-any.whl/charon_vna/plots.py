# %% imports
from typing import Callable, List, Literal, Tuple

import numpy as np
import xarray as xr
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.lines import Line2D
from matplotlib.ticker import EngFormatter
from numpy import typing as npt
from PySide6.QtWidgets import QVBoxLayout, QWidget
from skrf import plotting as rf_plt

from charon_vna.util import db20, s2vswr

__all__ = ("PlotWidget",)


# %%
class PlotWidget(QWidget):
    traces: List[Tuple[int | str]]
    lines: List[Line2D]

    def __init__(self, type_: str = "logmag"):
        super().__init__()

        self.traces = [(1, 1)]

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.fig = plt.Figure(figsize=(5, 4), dpi=100, tight_layout=True)
        self.ax = self.fig.add_subplot(111)
        self.set_plot_type(type_)
        self.lines = [
            self.ax.plot([np.nan], [np.nan], label="$S_{" + str(m) + str(n) + "}$")[0] for m, n in self.traces
        ]
        self.ax.legend(loc="upper right")

        canvas = FigureCanvasQTAgg(self.fig)
        layout.addWidget(canvas)

        # toolbar = QToolBar("Toolbar")
        # toolbar.addAction("blah")
        # self.addToolBar(toolbar)

    def set_plot_type(
        self,
        type_: Literal["logmag", "phase", "vswr", "smith"],
        sweep_type: Literal["frequency", "time"] = "frequency",
    ) -> None:
        if sweep_type != "frequency":
            raise NotImplementedError("Only frequency sweeps are currently supported")

        if type_ == "logmag":
            self.setup_logmag()
        elif type_ == "phase":
            self.setup_phase()
        elif type_ == "vswr":
            self.setup_vswr()
        elif type_ == "smith":
            self.setup_smith()
        else:
            raise ValueError(f"Unknown plot type: {type_}")

        self._plot_type = type_

    def update_plot(self, data: xr.DataArray):
        if self._plot_type == "logmag":
            self.update_logmag(data)
        elif self._plot_type == "phase":
            self.update_phase(data)
        elif self._plot_type == "vswr":
            self.update_vswr(data)
        elif self._plot_type == "smith":
            self.update_smith(data)

    def setup_rect(self) -> None:
        self.ax.grid(True)
        self.ax.xaxis.set_major_formatter(EngFormatter())
        self.ax.set_xlabel("Frequency [Hz]")

    def update_rect(self, data: xr.DataArray, func: Callable[[npt.ArrayLike], npt.ArrayLike]) -> None:
        self.ax.set_xlim(data["frequency"].min().data, data["frequency"].max().data)
        for ii, (m, n) in enumerate(self.traces):
            self.lines[ii].set_xdata(data["frequency"])
            self.lines[ii].set_ydata(func(data.sel(m=m, n=n)))

        self.fig.canvas.draw()

    def setup_logmag(self, ylim: List[float] = [-30, 30]) -> None:
        self.setup_rect()
        self.ax.set_ylim(ylim)
        self.ax.set_ylabel("Amplitude [dB]")

    def update_logmag(self, data: xr.DataArray) -> None:
        self.update_rect(data, db20)

    def setup_phase(self) -> None:
        self.setup_rect()
        self.ax.set_ylim(-200, 200)
        self.ax.set_ylabel("Phase [deg]")

    def update_phase(self, data: xr.DataArray):
        self.update_rect(data, lambda s: np.angle(s, deg=True))

    def setup_vswr(self) -> None:
        self.setup_rect()
        self.ax.set_yticks(np.arange(1, 11))
        self.ax.set_ylim(1, 10)
        self.ax.set_ylabel("VSWR")

    def update_vswr(self, data: xr.DataArray) -> None:
        self.update_rect(data, s2vswr)

    def setup_smith(self) -> None:
        self.ax.grid(False)
        self.ax.set_xlim(-1, 1)
        self.ax.set_ylim(-1, 1)
        self.ax.set_aspect("equal")
        rf_plt.smith(ax=self.ax, smithR=1, chart_type="z", draw_vswr=None)

    def update_smith(self, data: xr.DataArray) -> None:
        for ii, (m, n) in enumerate(self.traces):
            sel = data.sel(m=m, n=n)
            self.lines[ii].set_xdata(sel.real)
            self.lines[ii].set_ydata(sel.imag)

        self.fig.canvas.draw()
