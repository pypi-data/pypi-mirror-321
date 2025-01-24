import matplotlib.pyplot as plt

# Color palette suitable for color vision deficiency
COLORS = {
    "primary": "#0077BB",  # Blue
    "secondary": "#EE7733",  # Orange
    "tertiary": "#009988",  # Teal
    "quaternary": "#CC3311",  # Red
    "quinary": "#33BBEE",  # Cyan
    "gray": "#BBBBBB",  # Gray
}

# Standard sizes for different figure elements
SIZES = {
    "figure": (6, 4),  # Standard figure size in inches
    "font": {"tiny": 8, "small": 12, "medium": 16, "large": 20, "xlarge": 24},
    "linewidth": 1.5,
    "markersize": 6,
    "tick_length": 4,
}


def set_style(font_scale=1.0):
    """
    Set the default style for all subsequent plots.

    Parameters:
    -----------
    font_scale : float
        Scale factor for all font sizes (default: 1.0)
    """
    plt.style.use("seaborn-v0_8-whitegrid")

    # Set font properties
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["font.sans-serif"] = ["Arial"]
    plt.rcParams["font.size"] = SIZES["font"]["medium"] * font_scale

    # Set figure properties
    plt.rcParams["figure.figsize"] = SIZES["figure"]
    plt.rcParams["figure.dpi"] = 300

    # Set axes properties
    plt.rcParams["axes.linewidth"] = SIZES["linewidth"]
    plt.rcParams["axes.labelsize"] = SIZES["font"]["large"] * font_scale
    plt.rcParams["axes.titlesize"] = SIZES["font"]["xlarge"] * font_scale

    # Set tick properties
    plt.rcParams["xtick.major.size"] = SIZES["tick_length"]
    plt.rcParams["ytick.major.size"] = SIZES["tick_length"]
    plt.rcParams["xtick.labelsize"] = SIZES["font"]["medium"] * font_scale
    plt.rcParams["ytick.labelsize"] = SIZES["font"]["medium"] * font_scale

    # Set legend properties
    plt.rcParams["legend.fontsize"] = SIZES["font"]["small"] * font_scale
    plt.rcParams["legend.frameon"] = True
    plt.rcParams["legend.edgecolor"] = "gray"

    # Set grid properties
    plt.rcParams["grid.linewidth"] = 0.5
    plt.rcParams["grid.alpha"] = 0.3


def apply_style(ax, title=None, xlabel=None, ylabel=None, legend=True):
    """
    Apply the journal style to a specific axes object.

    Parameters:
    -----------
    ax : matplotlib.axes.Axes
        The axes object to style
    title : str, optional
        Title for the plot
    xlabel : str, optional
        Label for x-axis
    ylabel : str, optional
        Label for y-axis
    legend : bool, optional
        Whether to show the legend (default: True)
    """
    # Set labels if provided
    if title:
        ax.set_title(title)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)

    # Configure legend
    if legend and ax.get_legend():
        ax.legend(frameon=True, edgecolor="gray")

    # Configure grid
    ax.grid(True, alpha=0.3, linewidth=0.5)

    # Set spine visibility and width
    for spine in ax.spines.values():
        spine.set_linewidth(SIZES["linewidth"])
