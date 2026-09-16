# Data Dictionary

## Synthetic trade dataset

| Field | Meaning | Analytical use |
|---|---|---|
| trade_id | Unique synthetic trade identifier | Validation and traceability |
| date | Trade date | Time-series analysis |
| strategy | Trading strategy label | Strategy comparison |
| instrument | Synthetic instrument label | Instrument contribution |
| session | Trading session | Session segmentation |
| market_regime | Synthetic market regime | Regime analysis |
| risk_amount | Capital/risk amount assigned to trade | Risk normalization |
| gross_pnl | P&L before execution costs | Gross performance |
| spread_cost | Synthetic spread assumption | Execution-cost analysis |
| slippage_cost | Synthetic slippage assumption | Execution-cost analysis |
| commission | Synthetic commission assumption | Execution-cost analysis |
| total_cost | Sum of execution-cost assumptions | Gross-to-net bridge |
| pnl | Net trade profit or loss after modeled costs | Net performance measurement |
| return_on_risk_pct | Net P&L relative to risk amount | Risk-adjusted trade efficiency |
| outcome | Win or loss classification based on net P&L | Win-rate and streak analysis |

## Historical market dataset

The optional Forex validation path downloads public daily OHLC observations for EURUSD. It does not commit downloaded market data to the repository.

| Field | Meaning | Analytical use |
|---|---|---|
| date | Daily market observation date | Time-series ordering |
| symbol | Public market symbol | Instrument identification |
| open/high/low/close | Daily OHLC prices | Signal and backtest inputs |
| volume | Provider-reported volume field where available | Context only; not treated as centralized FX volume |

## Derived risk measures

- **Equity:** cumulative net P&L used for portfolio analytics in this project.
- **Drawdown:** equity minus the prior running peak.
- **Maximum drawdown:** largest peak-to-trough equity decline.
- **VaR 95%:** fifth percentile of trade P&L, used as a trade-level loss threshold.
- **CVaR 95%:** average P&L of trades at or below the VaR threshold.
- **Recovery factor:** total P&L divided by absolute maximum drawdown when maximum drawdown is negative.
- **Negative P&L standard deviation:** standard deviation of losing-trade P&L; this is a dispersion measure for losing trades, not conventional target-based downside deviation.
- **Sharpe-style proxy:** trade-level return/risk statistic used for comparative analysis; it is not annualized.

## Position sizing and exposure measures

The dashboard's exposure calculator uses explicit, broker-agnostic assumptions:

- **Risk budget:** account equity × risk % / 100.
- **Position size:** risk budget / (stop distance × value per unit).
- **Notional exposure:** position size × entry price × contract size.
- **Margin requirement:** notional exposure / leverage.
- **Exposure %:** notional exposure / account equity × 100.
- **Leverage ratio:** notional exposure / account equity.
- **Exposure limit check:** PASS when exposure % is less than or equal to the configured maximum exposure %; otherwise BREACH.

Inputs are validated so non-positive or invalid values are rejected. The formulas are intended for transparent portfolio-analysis demonstrations and do not replace broker-specific margin, contract, or currency-conversion rules.

## Backtest assumptions

The historical validation strategy uses lagged moving-average signals so the current close is not used to trade at that same close. Spread, slippage, commission, position size, and moving-average windows are explicit assumptions and are not broker quotes.

The synthetic dataset is fixed-seed and contains no private trading, client, broker, or employer data. Public-market data is used only for historical validation; neither dataset represents live performance.
