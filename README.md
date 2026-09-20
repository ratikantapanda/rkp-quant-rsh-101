# rkp-quant-rsh-101

This repository is a single quant research monorepo for all research types, including macro, micro, alternative data, fundamentals, market data, and strategy work. The idea is to keep every research stream under one roof while still separating work by domain so you can scale from FRED and market data studies to factor research, event studies, and signal evaluation without creating fragmented projects.

## Research mindset
A strong quant workflow is not just notebook experimentation. It is:
1. Define the question.
2. Acquire clean data.
3. Build a reproducible pipeline.
4. Validate the assumptions.
5. Run a small proof-of-concept study.
6. Document findings and next steps.

## Data sources this monorepo supports
This repo is intended to support multiple quant data families, such as:
- macro and economic data: FRED, Central Bank feeds, government stats
- market data: OHLCV, order books, futures, options, FX, crypto
- fundamentals: company financials, earnings, valuation, sector data
- alternative data: sentiment, news, web traffic, satellite, geospatial, supply-chain
- proprietary or internal data: research outputs, generated factor tables, client files
- tick or event data for research and strategy experiments

The exact source does not matter; the workflow remains the same: ingest, validate, transform, analyze, and document.

## Monorepo structure

```text
rkp-quant-rsh-101/
├── README.md
├── pyproject.toml
├── requirements.txt
├── .gitignore
├── docs/
│   └── coding_standards.md
├── src/
│   └── rkp_quant_rsh_101/
│       ├── __init__.py
│       ├── config.py
│       ├── data/
│       │   ├── __init__.py
│       │   └── fred_client.py
│       └── analysis/
│           └── __init__.py
├── macro/
│   ├── README.md
│   └── fred_research/
│       └── __init__.py
├── micro/
│   ├── README.md
│   └── equity_research/
│       └── __init__.py
├── shared/
│   └── README.md
├── poc/
│   ├── 01_fred_data_pull.py
│   └── 02_fred_macro_analysis.py
├── tests/
│   └── test_config.py
├── data/
│   └── .gitkeep
├── outputs/
│   └── .gitkeep
└── notebooks/
    └── .gitkeep
```

## Why this monorepo style is better
Using one repo for all quant research gives you:
- one place for all research artifacts
- shared standards across macro and micro work
- easier reuse of configs, validation utilities, and plotting helpers
- cleaner cross-domain thinking, especially when macro variables affect equities
- less friction when moving from idea to POC to production research

## Recommended split
- `macro/` = macro, rates, inflation, growth, cycle, FRED work
- `micro/` = equity factors, stock-level signals, company research, screening
- `shared/` = reusable utilities, validation, logging, plotting, and cross-domain tools

This gives you a professional structure without forcing every project into one single folder.

## Domain folders
- `macro/` → macro, rates, inflation, growth, and economic cycle research
- `micro/` → stocks, cross-sectional factors, screening, and company-level research
- `signal/` → signal generation, feature transforms, and event-based indicators
- `factor/` → factor construction, scoring, calibration, and cross-sectional research
- `alpha/` → alpha idea generation, selection, ranking, and alpha decay testing
- `strategy/` → strategy logic, portfolio construction, and execution intent
- `backtest/` → historical simulation, performance attribution, and trade-level evaluation
- `risk/` → risk monitoring, drawdown control, factor exposure, and stress testing
- `shared/` → common utility code, validation, logging, and plotting
- `poc/` → quick experiments across any data source
- `notebooks/` → exploration notebooks for new ideas and dataset diagnostics

## Research-to-trading pipeline
The professional quant workflow is:

`Data ingestion → validation → feature engineering → signal generation → factor research → alpha research → strategy design → backtest → risk monitoring → execution planning`

This is the full pipeline that should live in one repo, not scattered across disconnected experiments.

## Setup

```bash
cd rkp-quant-rsh-101
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

## FRED setup
You need a FRED API key.

```bash
export FRED_API_KEY="your_key_here"
```

## Research process

### Step 1: Define a clear hypothesis
Examples:
- The yield curve slope predicts a recession regime.
- Inflation persistence affects risk appetite.
- Equity momentum differs systematically across macro regimes.

### Step 2: Data contract
For each dataset, record:
- series ID or ticker
- data definition
- frequency
- date range
- transform applied
- source and update time

### Step 3: Ingest and validate
Use the shared data client or workstream-specific wrapper to pull data and validate missing values, duplicates, and schema issues.

### Step 4: Build a POC
Use scripts in `poc/` or component-specific research directories to test the idea quickly.

### Step 5: Document and decide
If the POC is promising, promote it to a more structured module or notebook, and keep the results reproducible.

## Example workstreams
- Macro: FRED inflation, yields, unemployment, growth analysis
- Micro: equity quality, momentum, liquidity, volatility factors
- Cross-domain: macro regime filters for stock signal construction

## Suggested coding standard
Follow the rules in `docs/coding_standards.md`.

## Validation

```bash
python -m compileall src tests poc
PYTHONPATH=src pytest -q
```

## Professional recommendation
Use one monorepo, but separate workstreams by research domain. That is the right balance between organization and flexibility for a serious quant research workflow.
