# Trading Risk & Performance Analytics

## Trade-level performance → execution-aware risk → decision support

A recruiter-ready **financial analytics** project that evaluates trading performance, drawdowns, tail risk, execution costs, concentration, strategy behavior, and market-regime differences using Python, SQL, statistical analysis, and visual reporting.

> **Recruiter takeaway:** this project separates headline profitability from the risk, cost, and behavior underneath it.

## Interactive Dashboard

Run the project locally:

```bash
pip install -r requirements.txt
streamlit run app.py
```

The dashboard includes:

- Synthetic fixed-seed trade analytics for reproducible portfolio demonstrations
- Net-vs-gross P&L with explicit spread, slippage, and commission assumptions
- Equity and drawdown views
- Strategy and market-regime segmentation
- Tail-risk metrics including CVaR
- An optional **historical EURUSD validation path** using public daily market data
- A simple moving-average backtest with lagged signals and configurable execution-cost assumptions

The historical path is deliberately separated from the synthetic dataset. It validates that the analytics workflow can operate on public market observations without presenting backtest output as live or broker performance.

## The Business Problem

A positive P&L number does not explain whether performance is efficient, concentrated, volatile, exposed to tail losses, or eroded by execution costs. This project builds a reproducible framework for answering those questions from trade-level data and provides a bridge from public market data to simulated trades.

### Questions the analysis answers

- What are total P&L, win rate, profit factor, and expectancy?
- How deep and persistent are drawdowns?
- What do VaR and CVaR reveal about tail losses?
- How much gross performance is consumed by execution costs?
- Is performance dependent on a small group of winning trades?
- Which strategies, instruments, sessions, or regimes behave differently?
- Does a simple historical strategy remain profitable after explicit cost assumptions?
- Where should risk controls or further validation be prioritized?

## Executive View

| Lens | Measures | Decision question |
|---|---|---|
| **Performance** | Gross/net P&L, average trade, win rate | Is performance positive after costs? |
| **Efficiency** | Profit factor, expectancy | How efficient is the return profile? |
| **Downside** | Max drawdown, volatility, CVaR | How severe are adverse outcomes? |
| **Execution** | Spread, slippage, commission | How much return is consumed by trading costs? |
| **Recovery** | Recovery factor | How efficiently is drawdown recovered? |
| **Concentration** | Top-winner contribution | Is performance dependent on a few trades? |
| **Consistency** | Loss streaks, variability | How stable is the outcome distribution? |
| **Segmentation** | Strategy, instrument, session, regime | Where does behavior change? |

## Historical Forex Validation

The repository includes an optional public-data validation layer:

```text
Public EURUSD market data
        ↓
OHLC validation
        ↓
Lagged moving-average signal
        ↓
Position / trade simulation
        ↓
Gross P&L
        ↓
Spread + slippage + commission
        ↓
Net P&L
        ↓
Drawdown / risk summary
```

The implementation is intentionally simple. The purpose is to demonstrate **market-data ingestion, look-ahead control, execution-cost modeling, and reproducible analytics**, not to claim a production trading strategy.

## Visual Analysis

The key charts are generated from the fixed-seed synthetic dataset and committed as SVG:

![Cumulative Trading P&L](visualizations/equity_curve.svg)

![Trading Drawdown](visualizations/drawdown.svg)

![Total P&L by Strategy](visualizations/strategy_pnl.svg)

![Average P&L by Market Regime](visualizations/regime_avg_pnl.svg)

**[Open the Executive Risk Dashboard](reports/executive_dashboard.md)** for the KPI and decision framework.

## Analytical Workflow

```text
Synthetic Trade Data
        ↓
Validation & Cleaning
        ↓
Gross P&L → Execution Costs → Net P&L
        ↓
Performance → Drawdown & Tail Risk
        ↓
Concentration → Strategy / Instrument / Session / Regime Segmentation
        ↓
Public Forex Data → Lagged Signal → Cost-Aware Backtest
        ↓
SQL + Visual Reporting
        ↓
Risk-Control Questions
```

## What This Demonstrates

**Performance analytics** — gross/net P&L, win rate, profit factor, expectancy, average trade.

**Risk analytics** — drawdown, downside deviation, VaR/CVaR, volatility, recovery factor.

**Execution-aware analysis** — explicit spread, slippage, and commission assumptions so gross and net results can be compared.

**Market validation** — public EURUSD daily data, lagged signals, reproducible backtest parameters, and transparent cost assumptions.

**Segmentation** — strategy, instrument, session, and market regime.

**Statistical discipline** — the Sharpe-style measure is explicitly treated as a trade-level proxy, not an annualized Sharpe ratio.

**Business communication** — `Return → execution costs → downside → concentration → segmentation → validation → risk-control question`.

## Tech Stack

**Python · pandas · NumPy · SQL · Matplotlib · Git/GitHub · GitHub Actions · pytest · Streamlit**

## Reproduce It

Core portfolio pipeline (no network required):

```bash
pip install -r requirements.txt
python src/generate_data.py
python src/clean_data.py
python src/performance_analysis.py
python src/risk_analysis.py
python src/create_visualizations.py
pytest -q
```

Optional public-market validation:

```bash
python src/market_data.py
python src/backtest.py
```

The optional market-data commands require network access. They write downloaded data under `data/market/` and are not required for the fixed-seed synthetic workflow.

## Repository Map

| Folder / File | Purpose |
|---|---|
| `app.py` | Interactive Streamlit dashboard |
| `src/market_data.py` | Public historical Forex data ingestion |
| `src/backtest.py` | Lagged, cost-aware market backtest |
| `src/risk_analysis.py` | Drawdown and tail-risk metrics |
| `reports/` | Executive risk interpretation |
| `visualizations/` | Recruiter-visible charts |
| `sql/` | Reusable business analysis queries |
| `src/` | Data generation, validation, and analytics pipeline |
| `tests/` | Automated validation |
| `.github/workflows/` | CI quality checks |

## Data Integrity & Limitations

The core portfolio dataset is **synthetic**, fixed-seed, and created for reproducible demonstration. No private client, employer, brokerage, or account data is used.

The historical validation path uses public market observations, but the strategy is deliberately simplified and its spread, slippage, commission, position size, and signal parameters are assumptions. Historical backtests are not evidence of future performance.

The project does **not** claim live execution, broker connectivity, institutional risk limits, or production portfolio-management functionality. Those are intentionally outside the scope of this portfolio demonstration.

Results are not investment advice.

## Portfolio

Part of a three-project analytics portfolio:

- **Macro Market Intelligence** — economic and market context
- **Trading Risk & Performance Analytics** — financial risk, execution-aware performance, and historical-market validation
- **Customer Support Analytics** — business and operations analytics
