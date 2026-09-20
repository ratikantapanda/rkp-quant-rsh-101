from __future__ import annotations

import numpy as np
import pandas as pd

from rkp_quant_rsh_101.config import DEFAULT_SERIES
from rkp_quant_rsh_101.data.fred_client import FREDDataClient, validate_macro_frame


def add_stationary_transforms(frame: pd.DataFrame) -> pd.DataFrame:
    out = frame.copy()
    out["fed_funds_12m_change"] = out["fed_funds"].pct_change(12)
    out["cpi_12m_change"] = out["cpi"].pct_change(12)
    out["term_spread"] = out["treasury_10y"] - out["treasury_3m"]
    out["unemployment_gap"] = out["unemployment"] - out["unemployment"].rolling(12).mean()
    return out


def summarize_regime(frame: pd.DataFrame) -> pd.DataFrame:
    summary = pd.DataFrame({
        "mean": frame.mean(),
        "std": frame.std(),
        "min": frame.min(),
        "max": frame.max(),
    })
    return summary.round(4)


def main() -> None:
    client = FREDDataClient()
    raw = client.fetch_many(DEFAULT_SERIES, start="2010-01-01", frequency="m")
    data = validate_macro_frame(raw)
    prepared = add_stationary_transforms(data)

    print("Summary stats")
    print(summarize_regime(prepared[["fed_funds", "cpi", "unemployment", "term_spread"]]).head(20))

    output_path = "outputs/fred_macro_analysis.csv"
    prepared.to_csv(output_path)
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()
