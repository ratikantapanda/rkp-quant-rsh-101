from __future__ import annotations

import pandas as pd

from rkp_quant_rsh_101.config import DEFAULT_SERIES
from rkp_quant_rsh_101.data.fred_client import FREDDataClient, validate_macro_frame


def main() -> None:
    client = FREDDataClient()
    df = client.fetch_many(DEFAULT_SERIES, start="2010-01-01", frequency="m")
    df = validate_macro_frame(df)

    print(df.head())
    print(f"\nRows: {len(df)}")
    print(f"Columns: {list(df.columns)}")

    output_path = "outputs/fred_macro_data.csv"
    df.to_csv(output_path)
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()
