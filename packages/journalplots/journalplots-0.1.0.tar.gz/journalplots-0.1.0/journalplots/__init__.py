"""
journalplots
============

A Python package for creating publication-ready matplotlib figures with consistent
styling. Provides pre-configured color palettes, font sizes, and styling functions
optimized for scientific journals.

Features:
- Colorblind-friendly color palettes
- Journal-appropriate font sizes and styles
- High-resolution output settings
- Easy-to-use styling functions
- Consistent figure dimensions
"""

from .style import COLORS, SIZES, apply_style, set_style

__version__ = "0.1.0"
__author__ = "Baljyot Singh Parmar"
__email__ = "baljyotparmar@hotmail.com"

__all__ = [
    "set_style",
    "apply_style",
    "COLORS",
    "SIZES",
]
