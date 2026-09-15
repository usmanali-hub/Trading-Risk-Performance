# Methodology

## Dataset

The project generates 1,200 synthetic trade records covering multiple instruments, strategies, trading sessions, and market regimes. The synthetic data is intentionally reproducible with a fixed random seed.

## Validation

The cleaning layer validates required columns, parses dates, converts numeric fields, removes duplicate trade IDs, removes invalid non-positive risk amounts, and derives the final outcome from P&L.

## Performance

Performance is evaluated using total P&L, win rate, average trade P&L, average win, average loss, profit factor, expectancy, and return on risk.

## Risk

Risk is evaluated using cumulative equity, maximum drawdown, drawdown percentage, P&L variability, downside deviation, largest gain/loss, consecutive loss streaks, and average risk allocation.

## Segmentation

Results are compared by strategy, instrument, trading session, and market regime to identify concentration and performance differences.

## Important Limitation

This is an analytical demonstration, not a live trading recommendation. Synthetic results do not represent actual broker execution, transaction costs, slippage, liquidity, or future performance.
