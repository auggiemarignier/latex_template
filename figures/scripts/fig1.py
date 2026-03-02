"""Generate Figure 1: ______________."""

import matplotlib.pyplot as plt
import numpy as np
import scienceplots
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from utils import DATA_PATH, save_figure

plt.style.use("science")


def load_data() -> tuple[np.ndarray, np.ndarray]:
    """Load data for the figure."""
    return np.array([0, 1]), np.array([0, 1])


def create_figure(x: np.ndarray, y: np.ndarray) -> Figure:
    """Create the figure."""
    fig, ax = plt.subplots()
    ax.plot(x, y, label="Example Line")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Figure 1: Example Plot")
    ax.legend()
    return fig


def main() -> None:
    """Main function to generate the figure."""
    x, y = load_data()
    fig = create_figure(x, y)
    save_figure(fig, "figure1")


if __name__ == "__main__":
    main()
