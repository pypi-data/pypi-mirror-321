import json
import subprocess

import numpy as np

from charon_vna.gui import DEFAULT_CONFIG

config = dict(
    frequency=np.linspace(80e6, 500e6, 500).tolist(),
    power=-5,
)

with open(DEFAULT_CONFIG, "w") as f:
    json.dump(config, f)

# autoformat
subprocess.run(
    [
        "python",
        "-m",
        "json.tool",
        DEFAULT_CONFIG.resolve().as_posix(),
        DEFAULT_CONFIG.resolve().as_posix(),
    ]
)
