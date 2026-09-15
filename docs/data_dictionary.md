# Data Dictionary

| Field | Meaning | Analytical use |
|---|---|---|
| trade_id | Unique synthetic trade identifier | Validation and traceability |
| date | Trade date | Time-series analysis |
| strategy | Trading strategy label | Strategy comparison |
| instrument | Synthetic instrument label | Instrument contribution |
| session | Trading session | Session segmentation |
| market_regime | Synthetic market regime | Regime analysis |
| risk_amount | Capital/risk amount assigned to trade | Risk normalization |
| pnl | Trade profit or loss | Performance measurement |
| return_on_risk_pct | P&L relative to risk amount | Risk-adjusted trade efficiency |
| outcome | Win or loss classification | Win-rate and streak analysis |

## Derived risk measures

- Equity: cumulative P&L.
- Drawdown: equity minus prior peak equity.
- Maximum drawdown: largest peak-to-trough equity decline.
- VaR 95%: fifth percentile of trade P&L, used as a trade-level loss threshold.
- CVaR 95%: average P&L of trades below the VaR threshold.
- Recovery factor: total P&L divided by absolute maximum drawdown when drawdown is non-zero.

All records are synthetic and are not private trading, client, broker, or employer data.
