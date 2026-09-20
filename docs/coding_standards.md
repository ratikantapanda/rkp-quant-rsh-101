# Coding Standards for Quant Research

## 1. Research workflow
- Start with a single, well-defined question.
- Keep an experiment log: hypothesis, data source, method, result, and next step.
- Separate raw data, curated data, and analysis outputs in distinct folders.
- Never mix exploration, production code, and final reporting.

## 2. Code structure
- Use clear package names: `src/<project_name>/`
- Keep data access in `data/`, analysis logic in `analysis/`, and outcomes in `outputs/`
- Prefer small functions with single responsibilities
- Use explicit names like `fetch_fred_series`, `compute_zscore`, `build_signal_frame`

## 3. Documentation
- Add docstrings to public functions and classes
- Record assumptions, data definitions, and transformation logic in code comments
- Keep notebooks for exploration only; move reusable logic into source files

## 4. Data quality
- Validate schema before modeling
- Check missing values, duplicates, and outliers at ingestion time
- Keep a reproducible metadata table for series IDs, source names, and dates

## 5. Testing
- Add unit tests for data validation, signal generation, and transformation logic
- Validate that research scripts fail clearly when configuration is missing
- Prefer deterministic tests over brittle statistical expectations

## 6. Reproducibility
- Pin versions in `requirements.txt` or `pyproject.toml`
- Store raw configuration and research parameters in code or config files
- Treat results as reproducible evidence, not as ad hoc plots

## 7. Professional quant hygiene
- Use a clear naming convention for research notebooks: `01_ingest`, `02_explore`, `03_model`, `04_report`
- Keep the codebase lean and readable
- Write logic in a way that can survive review by a quant team or PM
