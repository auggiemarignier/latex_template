"""Common utilities for figure generation."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.figure import Figure

DATA_PATH = Path(__file__).parent.parent / "data"
OUTPUT_PATH = Path(__file__).parent.parent / "generated"


def save_figure(fig: Figure, filename: str) -> None:
    """Save a figure to a file."""
    for ext in [".pdf", ".png"]:
        fig.savefig(str(OUTPUT_PATH / f"{filename}{ext}"), bbox_inches="tight", dpi=300)
    plt.close(fig)
