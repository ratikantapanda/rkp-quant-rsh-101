from __future__ import annotations

from typing import Iterable

import pandas as pd
from fredapi import Fred

from rkp_quant_rsh_101.config import DEFAULT_END, DEFAULT_FREQUENCY, DEFAULT_SERIES, DEFAULT_START, get_fred_api_key


class FREDDataClient:
    """Thin wrapper around the FRED API for research-grade macro data pulls."""

    def __init__(self, api_key: str | None = None) -> None:
        self.api_key = api_key or get_fred_api_key()
        self.client = Fred(api_key=self.api_key)

    def fetch_series(
        self,
        series_id: str,
        start: str = DEFAULT_START,
        end: str | None = DEFAULT_END,
        frequency: str = DEFAULT_FREQUENCY,
    ) -> pd.Series:
        """Fetch one FRED series and normalize to a pandas Series."""
        series = self.client.get_series(
            series_id,
            observation_start=start,
            observation_end=end,
            frequency=frequency,
        )
        if not isinstance(series, pd.Series):
            raise TypeError(f"Unexpected return type for series {series_id}: {type(series)!r}")
        return series.rename(series_id).sort_index()

    def fetch_many(
        self,
        series_map: dict[str, str] | None = None,
        start: str = DEFAULT_START,
        end: str | None = DEFAULT_END,
        frequency: str = DEFAULT_FREQUENCY,
    ) -> pd.DataFrame:
        """Fetch multiple FRED series into one DataFrame."""
        selected = series_map or DEFAULT_SERIES
        frame = pd.DataFrame({})
        for name, series_id in selected.items():
            series = self.fetch_series(series_id, start=start, end=end, frequency=frequency)
            frame[name] = series
        return frame.sort_index()


def validate_macro_frame(frame: pd.DataFrame) -> pd.DataFrame:
    """Basic validation for macro research data quality."""
    if frame.empty:
        raise ValueError("FRED data frame is empty.")

    missing = frame.isna().sum()
    if missing.any():
        raise ValueError(f"Missing values found in FRED data: {missing.to_dict()}")

    if frame.index.has_duplicates:
        raise ValueError("Duplicate index values found in the FRED frame.")

    return frame.copy()
