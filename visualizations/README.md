# Visualizations

Run `python src/create_visualizations.py` after generating and cleaning the dataset.

The script creates four portfolio-ready charts:

- `equity_curve.png` — cumulative P&L over the trading history
- `drawdown.png` — distance from the running equity peak
- `strategy_pnl.png` — total P&L contribution by strategy
- `regime_avg_pnl.png` — average trade P&L by market regime

PNG outputs are intentionally ignored by Git so they can be regenerated locally from the reproducible pipeline.
