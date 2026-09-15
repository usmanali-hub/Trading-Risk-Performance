# Trading Risk & Performance Analytics

## Trade-level performance → risk-aware decisions

A reproducible financial analytics project that evaluates **performance, risk, drawdowns, expectancy, tail losses, concentration, and strategy behavior** using Python, SQL, statistical analysis, and visual reporting.

### Why this project matters

Headline P&L can hide fragile performance. This project separates **return, efficiency, downside risk, drawdown, concentration, and segment behavior** so an analyst can investigate where performance is actually coming from.

## Business Questions

- Which strategies and instruments produce the strongest risk-adjusted behavior?
- What are win rate, profit factor, expectancy, and average return per trade?
- How deep and persistent are drawdowns?
- What do VaR and CVaR reveal about tail losses?
- Are results concentrated in a small number of winning trades?
- Which sessions and market regimes contribute most to performance?
- Where should risk controls or further investigation be prioritized?

## Analytical Workflow

```text
Synthetic Trade Data → Validation & Cleaning
        ↓
Performance Metrics → Drawdown & Tail Risk
        ↓
Concentration Analysis → Strategy / Instrument / Session / Regime Segmentation
        ↓
SQL → Visual Reporting → Decision Framework
```

## Advanced Analytics

| Area | Metrics |
|---|---|
| Performance | Total P&L, average trade, win rate, average win/loss |
| Efficiency | Profit factor, expectancy, return on risk |
| Risk | Max drawdown, drawdown %, P&L volatility, downside deviation |
| Tail risk | VaR 95%, CVaR 95% |
| Recovery | Recovery factor |
| Consistency | Loss streaks, variability |
| Concentration | Top-10%-winner P&L share |
| Segmentation | Strategy, instrument, session, market regime |

The Sharpe-style measure is deliberately labeled a **trade-level proxy** and is not presented as an annualized investment statistic.

## Tech Stack

**Python · pandas · NumPy · SQL · Matplotlib · Git/GitHub · GitHub Actions**

## Repository Structure

```text
├── data/                 # Synthetic dataset documentation
├── docs/                 # Methodology, dictionary, decision framework
├── notebooks/            # Analytical walkthrough
├── reports/              # Executive interpretation
├── sql/                  # Business analysis queries
├── src/                  # Generation, cleaning, performance, risk, visualization
├── visualizations/       # Chart documentation
├── .github/workflows/    # Automated quality checks
├── README.md
└── requirements.txt
```

## Reproducibility

```bash
pip install -r requirements.txt
python src/generate_data.py
python src/clean_data.py
python src/performance_analysis.py
python src/risk_analysis.py
python src/create_visualizations.py
```

The dataset uses a fixed random seed so the analytical workflow can be reproduced consistently. Generated data and charts are excluded from Git.

## Decision Framework

**Performance:** Start with P&L, expectancy, profit factor, and return on risk.

**Risk:** Evaluate drawdown, tail losses, volatility, streaks, and recovery.

**Concentration:** Check whether a small group of winners drives a disproportionate share of positive P&L.

**Segmentation:** Compare strategy, instrument, session, and market regime before drawing conclusions.

## Data Integrity

All trading records are **synthetic** and created for portfolio demonstration. No private client, employer, brokerage, or account data is included. Results are not investment advice or evidence of future performance.
