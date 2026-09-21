from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[2]
ENV_FILE = ROOT_DIR / ".env"
DATA_DIR = ROOT_DIR / "data"
OUTPUT_DIR = ROOT_DIR / "outputs"

load_dotenv(dotenv_path=ENV_FILE, override=False)
# Grouping multiple FRED series under single macro theme keys
MACRO_THEMES = {
    "monetary_policy": [
        "FEDFUNDS", 
        "WALCL"
    ],
    "inflation": [
        "CPIAUCSL", 
        "CPILFESL", 
        "T10YIE"
    ],
    "labor_market": [
        "UNRATE", 
        "PAYEMS"
    ],
    "interest_rates": [
        "DGS10", 
        "DGS3MO"
    ],
    "capital_markets": [
        "SP500", 
        "VIXCLS"
    ],
    "economic_growth": [
        "GDPC1"
    ]
}


macro_themes = {
    "Monetary Policy & Interest Rates": {
        "FEDFUNDS": "Federal Funds Effective Rate",
        "SOFR": "Secured Overnight Financing Rate",
        "WALCL": "Federal Reserve Total Assets (QE/QT)",
        "M2SL": "M2 Money Supply"
    },
    "Inflation & Price Stability": {
        "CPIAUCSL": "Consumer Price Index (Headline)",
        "CPILFESL": "Core CPI (Excluding Food & Energy)",
        "PCEPI": "Personal Consumption Expenditures Price Index",
        "PPIACO": "Producer Price Index (Wholesale Costs)"
    },
    "Economic Output & Growth": {
        "GDPC1": "Real Gross Domestic Product",
        "INDPRO": "Industrial Production Index",
        "DGORDER": "Durable Goods New Orders",
        "A939RX0Q048SBEA": "Real GDP per Capita"
    },
    "Labor Markets & Employment": {
        "UNRATE": "Unemployment Rate",
        "PAYEMS": "Nonfarm Payrolls",
        "JTSJOL": "JOLTS Job Openings",
        "ECI": "Employment Cost Index"
    },
    "Debt & Capital Markets": {
        "DGS10": "10-Year Treasury Yield",
        "DGS2": "2-Year Treasury Yield",
        "BAMLH0A0HYM2": "ICE BofA High Yield Spread",
        "GFDEGDQ188S": "Federal Debt as % of GDP"
    },
    "Housing & Real Estate": {
        "HOUST": "Housing Starts",
        "HSN1F": "New One-Family Houses Sold",
        "CSUSHPINSA": "S&P Case-Shiller Home Price Index",
        "MORTGAGE30US": "30-Year Fixed Mortgage Rate"
    },
    "Consumer Health & Retail Activity": {
        "RSXFS": "Advance Retail Sales",
        "PCE": "Personal Consumption Expenditures",
        "UMCSENT": "University of Michigan Consumer Sentiment",
        "PSAVERT": "Personal Saving Rate"
    },
    "International Trade & Global Macro": {
        "BOPGSTB": "Trade Balance (Goods and Services)",
        "NETEXP": "Net Exports",
        "DTWEXAFEGSMTH": "Nominal Broad Dollar Index"
    }
}


DEFAULT_SERIES = {
    "fed_funds": "FEDFUNDS",
    "cpi": "CPIAUCSL",
    "core_cpi": "CPILFESL",
    "unemployment": "UNRATE",
    "real_gdp": "GDPC1",
    "treasury_10y": "DGS10",
    "treasury_3m": "DGS3MO",
    "sp500": "SP500",
    "vix": "VIXCLS",
    "inflation": "T10YIE",
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
