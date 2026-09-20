"""Data access utilities for FRED-based macro research."""

from .fred_client import FREDDataClient, validate_macro_frame

__all__ = ["FREDDataClient", "validate_macro_frame"]
