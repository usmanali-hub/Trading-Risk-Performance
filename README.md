# Trading Risk & Performance Analytics

## Turning trade-level records into risk-aware decisions

A reproducible financial analytics project that evaluates **trading performance, risk, drawdowns, expectancy, and strategy behavior** using Python, SQL, statistical analysis, and visual reporting.

The objective is to move beyond headline P&L and answer a more useful question: **where is performance actually coming from, and what level of risk is required to produce it?**

## Business Questions

- Which strategies and instruments produce the strongest risk-adjusted behavior?
- What are the win rate, profit factor, expectancy, and average return per trade?
- How deep and persistent are drawdowns?
- Are results concentrated in a small number of trades?
- Which sessions contribute most to performance?
- How does strategy behavior change across market regimes?
- Where should risk controls or further investigation be prioritized?

## Analytical Workflow

```text
Synthetic Trade Data
        ↓
Validation & Cleaning
        ↓
Performance Metrics
        ↓
Risk & Drawdown Analysis
        ↓
Strategy / Instrument / Session / Regime Segmentation
        ↓
SQL Business Queries
        ↓
Visual Reporting
        ↓
Decision-Oriented Findings
```

## Key Metrics

| Area | Metrics |
|---|---|
| Performance | Total P&L, average trade, win rate, average win/loss |
| Efficiency | Profit factor, expectancy, return on risk |
| Risk | Maximum drawdown, drawdown %, volatility, downside deviation |
| Consistency | Loss streaks, variability, concentration |
| Segmentation | Strategy, instrument, session, market regime |

## Tech Stack

- **Python** — analytical pipeline and automation
- **pandas / NumPy** — data preparation and statistical calculations
- **SQL** — portfolio and trading-performance queries
- **Matplotlib** — performance and risk visualization
- **Git / GitHub** — version control and reproducibility

## Repository Structure

```text
├── data/                 # Dataset documentation; generated CSVs are ignored
├── docs/                 # Methodology and findings
├── notebooks/            # Analytical walkthrough
├── reports/              # Executive interpretation
├── sql/                  # Trading analysis queries
├── src/                  # Generation, cleaning, performance, risk, visualization
├── visualizations/       # Chart documentation; generated PNGs are ignored
├── .gitignore
├── requirements.txt
└── README.md
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

The dataset is generated with a fixed random seed so the analytical workflow can be reproduced consistently. Generated CSV and PNG outputs are excluded from Git.

## Data Integrity Note

The trading records are **synthetic** and created for portfolio demonstration. No private client, employer, brokerage, or account data is included. The results should not be interpreted as investment advice or evidence of future trading performance.

## What This Project Demonstrates

This project demonstrates practical Data Analyst skills across **financial analysis, risk measurement, data validation, segmentation, SQL, Python automation, statistical reasoning, visualization, and executive reporting**.

The emphasis is on explaining performance in context rather than presenting raw returns without a risk lens.
