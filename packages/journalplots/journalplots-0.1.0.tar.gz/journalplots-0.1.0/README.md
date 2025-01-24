# JournalPlots

A Python package for creating publication-ready matplotlib figures with consistent styling. Designed to make your scientific visualizations look professional and meet journal requirements.

## Features

- 🎨 Colorblind-friendly color palettes
- 📏 Journal-appropriate font sizes and styles
- 🖼️ High-resolution output settings (300 DPI)
- 🎯 Easy-to-use styling functions
- 📐 Consistent figure dimensions

## Installation

You can install the package directly from source:

```bash
git clone https://github.com/joemans3/journalplots.git
cd journalplots
pip install .
```

or use PyPI package:
```bash
pip install JournalPlots
```

## Usage

### Basic Usage

```python
import matplotlib.pyplot as plt
from journalplots import set_style, apply_style, COLORS

# Set the global style
set_style(font_scale=1.0)

# Create your plot
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 2, 3], color=COLORS['primary'], label='Data')
apply_style(ax, title='My Plot', xlabel='X', ylabel='Y')
plt.show()
```

### Available Colors

The package includes a colorblind-friendly palette:
```python
from journalplots import COLORS

# Available colors:
# - COLORS['primary']     # Blue (#0077BB)
# - COLORS['secondary']   # Orange (#EE7733)
# - COLORS['tertiary']    # Teal (#009988)
# - COLORS['quaternary']  # Red (#CC3311)
# - COLORS['quinary']     # Cyan (#33BBEE)
# - COLORS['gray']        # Gray (#BBBBBB)
```

### Customizing Sizes

You can adjust various size parameters:
```python
from journalplots import SIZES

# Available size presets:
# - SIZES['figure']       # Default figure size in inches
# - SIZES['font']         # Font sizes (tiny, small, medium, large, xlarge)
# - SIZES['linewidth']    # Default line width
# - SIZES['markersize']   # Default marker size
# - SIZES['tick_length']  # Length of axis ticks
```

### Style Functions

#### set_style()
Sets global matplotlib parameters for consistent styling:
```python
set_style(font_scale=1.0)  # Adjust font_scale to make all text larger or smaller
```

#### apply_style()
Apply styling to a specific axes object:
```python
apply_style(ax,
           title='My Plot',     # Optional plot title
           xlabel='X',          # Optional x-axis label
           ylabel='Y',          # Optional y-axis label
           legend=True)         # Whether to show legend
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
