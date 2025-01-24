"""
Perplexity Search - A Python tool for performing technical searches using the Perplexity API
"""

__version__ = "0.2.2"

from .core import perform_search, main
__all__ = ["perform_search", "main"]
