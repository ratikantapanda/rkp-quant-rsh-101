from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[2]
ENV_FILE = ROOT_DIR / ".env"
DATA_DIR = ROOT_DIR / "data"
OUTPUT_DIR = ROOT_DIR / "outputs"

load_dotenv(dotenv_path=ENV_FILE, override=False)

DEFAULT_SERIES = {
    "fed_funds": "FEDFUNDS",
    "cpi": "CPIAUCSL",
    "core_cpi": "CPILFESL",
    "unemployment": "UNRATE",
    "real_gdp": "GDPC1",
    "treasury_10y": "DGS10",
    "treasury_3m": "DGS3MO",
    "sp500": "SP500",
}

DEFAULT_START = "2010-01-01"
DEFAULT_END = None
DEFAULT_FREQUENCY = "m"


def get_env_var(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ValueError(f"{name} is not set. Add it to .env and activate the venv.")
    return value


def get_fred_api_key() -> str:
    return get_env_var("FRED_API_KEY")
