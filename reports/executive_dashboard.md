# Executive Risk Dashboard — Trading Risk & Performance

> **Trade-level performance → risk-aware decisions**

This is the recruiter-facing entry point for the analytical output. Charts are generated reproducibly from the synthetic trade dataset.

## Executive View

| Lens | KPI | Decision question |
|---|---|---|
| Return | Total P&L / average trade | Is the strategy generating positive contribution? |
| Efficiency | Profit factor / expectancy | Is the return profile efficient? |
| Downside | Max drawdown / CVaR 95% | How severe are adverse outcomes? |
| Recovery | Recovery factor | How efficiently is drawdown recovered? |
| Concentration | Top 10% winner share | Is performance dependent on a small group of trades? |
| Consistency | Loss streak / variability | How stable is the outcome distribution? |
| Segments | Strategy / instrument / session / regime | Where does behavior change? |

## Generated Visuals

Running `src/create_visualizations.py` creates:

- `equity_curve.png` — cumulative P&L path
- `drawdown.png` — drawdown from the running equity peak
- `strategy_pnl.png` — total P&L by strategy
- `regime_avg_pnl.png` — average trade P&L by market regime

## Risk Interpretation

1. Establish return and expectancy.
2. Quantify drawdown and tail losses.
3. Test concentration of positive P&L.
4. Segment results before making a strategy-level conclusion.
5. Identify the next risk-control or validation question.

### Important metric note

The Sharpe-style measure in this project is a **trade-level proxy**, not an annualized Sharpe ratio. VaR/CVaR are calculated from trade P&L and should be interpreted within that same dataset context.

## Data Integrity

- The dataset is synthetic and generated with a fixed seed.
- No private brokerage, client, employer, or account data is used.
- Results demonstrate analytical methodology; they are not claims about future trading performance.

## Reproduce

```bash
pip install -r requirements.txt
python src/generate_data.py
python src/clean_data.py
python src/performance_analysis.py
python src/risk_analysis.py
python src/create_visualizations.py
```

**Interview framing:** `Return → downside → concentration → segmentation → risk-control question.`
