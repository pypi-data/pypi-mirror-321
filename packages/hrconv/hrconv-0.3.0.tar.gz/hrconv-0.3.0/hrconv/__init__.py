# Expose user to hrc library
from .hrc import convolve_hrf, deconvolve_hrf
from .hrc import hrf
from .observer import lens

# Metadata
__all__ = ["convolve_hrf", "deconvolve_hrf", "hrf", "lens"]
__version__ = "0.3.0"
__author__ = "Denny Schaedig"