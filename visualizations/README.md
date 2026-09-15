# Visualizations

The portfolio charts are committed as SVG so they render directly on GitHub.

- `equity_curve.svg` — cumulative P&L over the trading history
- `drawdown.svg` — distance from the running equity peak
- `strategy_pnl.svg` — total P&L contribution by strategy
- `regime_avg_pnl.svg` — average trade P&L by market regime

Regenerate them with `python src/create_visualizations.py` after generating and cleaning the fixed-seed synthetic dataset.