# %% imports
from pathlib import Path

import click

# from charon_vna.vna import Charon


@click.command()
@click.argument("start", type=float)
@click.argument("stop", type=float)
@click.argument("pts", type=int)
@click.option("--ports", "-n", type=int, default=1, help="Number of ports.")
@click.option("--power", "-p", type=float, default=-5, help="Port output power [dBm].")
@click.option("--snp", "-o", type=click.Path(), help="Path for output Touchstone file.")
def capture(start: float, stop: float, pts: int, power: float, snp: Path, ports: int):
    raise NotImplementedError


# %%
def main():
    capture()


if __name__ == "__main__":
    main()
