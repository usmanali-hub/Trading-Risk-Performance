# Trading Performance Analysis Walkthrough

This notebook-style walkthrough documents the analytical sequence used by the project.

## 1. Generate the dataset

```bash
python src/generate_data.py
```

The generator creates 1,200 reproducible synthetic trades across three strategies, four instruments, three sessions, and three market regimes.

## 2. Validate the data

```bash
python src/clean_data.py
```

The cleaning step checks required fields, parses dates, validates numeric columns, removes duplicate trade IDs, and ensures risk amounts are positive.

## 3. Calculate performance

```bash
python src/performance_analysis.py
```

This produces `reports/performance_summary.csv`, segmented by strategy, instrument, session, and market regime.

## 4. Calculate risk

```bash
python src/risk_analysis.py
```

This produces `reports/risk_summary.csv` and measures maximum drawdown, variability, downside deviation, largest win/loss, and consecutive losses.

## 5. Produce visual evidence

```bash
python src/create_visualizations.py
```

The visualization layer produces an equity curve, drawdown chart, strategy P&L comparison, and market-regime comparison.

## 6. Analytical interpretation

The final question is not simply whether the strategy made money. The analyst should determine whether the result was consistent, what generated it, where risk accumulated, and whether performance depended on a particular market regime or segment.

> **Note:** All trade data is synthetic and intended for portfolio demonstration only.
