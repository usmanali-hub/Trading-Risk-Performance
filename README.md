# Trading Risk & Performance Analytics

A reproducible financial analytics project that evaluates trading performance, portfolio risk, drawdowns, expectancy, and strategy behavior using Python, SQL, and statistical analysis.

## Business Questions

- Which strategies and instruments generate the strongest risk-adjusted results?
- What is the win rate, profit factor, expectancy, and average return per trade?
- How large and how long are drawdowns?
- Are returns concentrated in a small number of trades?
- Which market sessions and setups contribute most to performance?
- How does performance change across market conditions?

## Analytical Workflow

Synthetic trade-level data → validation → performance metrics → risk metrics → segmentation → SQL analysis → visual reporting.

## Key Metrics

**Performance:** total P&L, return, win rate, average win/loss, profit factor, expectancy, cumulative equity.

**Risk:** maximum drawdown, drawdown duration, volatility, downside deviation, loss streaks, exposure concentration, and return variability.

## Data Note

The repository uses synthetic trading records designed for analytical demonstration. No private client, employer, brokerage, or account data is included.

## Skills Demonstrated

Python • pandas • NumPy • SQL • financial analysis • risk analytics • exploratory data analysis • data validation • statistical reasoning • visualization • reproducible analytics

## Repository Structure

```text
Trading-Risk-Performance/
├── data/
├── src/
│   ├── generate_data.py
│   ├── clean_data.py
│   ├── performance_analysis.py
│   └── risk_analysis.py
├── sql/
│   └── trading_analysis.sql
├── notebooks/
├── visualizations/
├── docs/
│   ├── methodology.md
│   └── findings.md
└── reports/
    └── executive_summary.md
```

## Reproducibility

Install dependencies with `pip install -r requirements.txt`, generate the synthetic dataset, then run the analysis scripts in order.
