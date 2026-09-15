# Trading Risk & Performance Analytics

## Trade-level performance → risk-aware decisions

A recruiter-ready **financial analytics** project that evaluates trading performance, drawdowns, tail risk, concentration, strategy behavior, and market-regime differences using Python, SQL, statistical analysis, and visual reporting.

> **Recruiter takeaway:** this project shows that I can separate headline performance from the risk and behavior underneath it.

## Interactive Dashboard

Run the project as an interactive local dashboard:

```bash
pip install -r requirements.txt
streamlit run app.py
```

The dashboard lets users filter by **strategy** and **market regime**, then explore P&L, win rate, profit factor, equity curve, and segment performance. The app automatically generates the fixed-seed synthetic dataset if it is not present.

For a hosted version, deploy `app.py` on any Streamlit-compatible hosting service.

## The Business Problem

A positive P&L number does not explain whether performance is efficient, concentrated, volatile, or vulnerable to large losses. This project builds a reproducible framework for answering those questions from trade-level data.

### Questions the analysis answers

- What are total P&L, win rate, profit factor, and expectancy?
- How deep and persistent are drawdowns?
- What do VaR and CVaR reveal about tail losses?
- Is performance dependent on a small group of winning trades?
- Which strategies, instruments, sessions, or regimes behave differently?
- Where should risk controls or further validation be prioritized?

## Executive View

| Lens | Measures | Decision question |
|---|---|---|
| **Performance** | P&L, average trade, win rate | Is performance positive? |
| **Efficiency** | Profit factor, expectancy | How efficient is the return profile? |
| **Downside** | Max drawdown, volatility, CVaR | How severe are adverse outcomes? |
| **Recovery** | Recovery factor | How efficiently is drawdown recovered? |
| **Concentration** | Top-winner contribution | Is performance dependent on a few trades? |
| **Consistency** | Loss streaks, variability | How stable is the outcome distribution? |
| **Segmentation** | Strategy, instrument, session, regime | Where does behavior change? |

## Visual Analysis

The key charts are visible directly on GitHub:

![Cumulative Trading P&L](visualizations/equity_curve.svg)

![Trading Drawdown](visualizations/drawdown.svg)

![Total P&L by Strategy](visualizations/strategy_pnl.svg)

![Average P&L by Market Regime](visualizations/regime_avg_pnl.svg)

These visuals are generated from the project's fixed-seed synthetic dataset and committed as SVG so a recruiter can inspect the analytical output without opening the source code.

**[Open the Executive Risk Dashboard](reports/executive_dashboard.md)** for the KPI and decision framework.

## Analytical Workflow

```text
Synthetic Trade Data
        ↓
Validation & Cleaning
        ↓
Performance Metrics → Drawdown & Tail Risk
        ↓
Concentration → Strategy / Instrument / Session / Regime Segmentation
        ↓
SQL + Visual Reporting
        ↓
Risk-Control Questions
```

## What This Demonstrates

**Performance analytics** — P&L, win rate, profit factor, expectancy, average trade.

**Risk analytics** — drawdown, downside deviation, VaR/CVaR, volatility, recovery factor.

**Segmentation** — strategy, instrument, session, and market regime.

**Statistical discipline** — the Sharpe-style measure is explicitly treated as a trade-level proxy, not an annualized Sharpe ratio.

**Business communication** — `Return → downside → concentration → segmentation → risk-control question`.

## Tech Stack

**Python · pandas · NumPy · SQL · Matplotlib · Git/GitHub · GitHub Actions · pytest · Streamlit**

## Reproduce It

```bash
pip install -r requirements.txt
python src/generate_data.py
python src/clean_data.py
python src/performance_analysis.py
python src/risk_analysis.py
python src/create_visualizations.py
pytest -q
```

## Repository Map

| Folder | Purpose |
|---|---|
| `app.py` | Interactive Streamlit dashboard |
| `reports/` | Executive risk interpretation |
| `visualizations/` | Recruiter-visible charts |
| `sql/` | Reusable business analysis queries |
| `src/` | Data generation and analytics pipeline |
| `tests/` | Automated validation |
| `.github/workflows/` | CI quality checks |

## Data Integrity

The dataset is **synthetic**, fixed-seed, and created for portfolio demonstration. No private client, employer, brokerage, or account data is used. Results are not investment advice or evidence of future performance.

## Portfolio

Part of a three-project analytics portfolio:

- **Macro Market Intelligence** — economic and market context
- **Trading Risk & Performance Analytics** — financial risk and performance
- **Customer Support Analytics** — business and operations analytics
