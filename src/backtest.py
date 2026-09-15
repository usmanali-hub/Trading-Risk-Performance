"""Simple, cost-aware historical market backtest.

This is a validation layer, not a claim of live trading performance. Signals
use only information available at the prior close; execution costs are
explicit assumptions so gross and net results can be compared.
"""
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def moving_average_backtest(
    market,
    fast_window=20,
    slow_window=50,
    units=10_000,
    spread_bps=1.0,
    slippage_bps=0.5,
    commission_per_100k=7.0,
):
    """Run a long/short moving-average backtest with explicit cost assumptions."""
    if fast_window >= slow_window:
        raise ValueError("fast_window must be smaller than slow_window")
    required = {"date", "close"}
    missing = required - set(market.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")

    x = market[["date", "close"]].copy().sort_values("date").dropna()
    x["fast_ma"] = x["close"].rolling(fast_window).mean()
    x["slow_ma"] = x["close"].rolling(slow_window).mean()

    # Keep the warm-up period flat. Once both averages exist, lag the signal
    # so today's position only uses information available at the prior close.
    raw_signal = pd.Series(0, index=x.index, dtype=float)
    valid = x["fast_ma"].notna() & x["slow_ma"].notna()
    raw_signal.loc[valid] = np.where(
        x.loc[valid, "fast_ma"] > x.loc[valid, "slow_ma"], 1, -1
    )
    x["position"] = raw_signal.shift(1).fillna(0)
    x["price_change"] = x["close"].diff().fillna(0)
    x["gross_pnl"] = x["position"] * x["price_change"] * units

    # Spread is paid on every position change; slippage scales with traded price.
    turnover = x["position"].diff().abs().fillna(x["position"].abs())
    spread_cost = turnover * (x["close"].abs() * spread_bps / 10_000) * units
    slippage_cost = turnover * (x["close"].abs() * slippage_bps / 10_000) * units
    commission = turnover * (units / 100_000) * commission_per_100k
    x["spread_cost"] = spread_cost
    x["slippage_cost"] = slippage_cost
    x["commission"] = commission
    x["net_pnl"] = x["gross_pnl"] - spread_cost - slippage_cost - commission
    x["equity_gross"] = x["gross_pnl"].cumsum()
    x["equity_net"] = x["net_pnl"].cumsum()
    return x


def backtest_summary(frame):
    """Return compact gross-vs-net performance metrics."""
    trades = frame.loc[frame["position"].ne(0)].copy()
    net = frame["net_pnl"]
    gross = frame["gross_pnl"]
    return {
        "observations": int(len(frame)),
        "position_days": int(len(trades)),
        "gross_pnl": float(gross.sum()),
        "net_pnl": float(net.sum()),
        "total_costs": float((gross - net).sum()),
        "net_win_rate_pct": float(net.loc[net.ne(0)].gt(0).mean() * 100) if net.ne(0).any() else 0.0,
        "max_net_drawdown": float((frame["equity_net"] - frame["equity_net"].cummax()).min()),
    }


if __name__ == "__main__":
    from market_data import download_daily

    data = download_daily()
    result = moving_average_backtest(data)
    out = ROOT / "data" / "market" / "eurusd_backtest.csv"
    result.to_csv(out, index=False)
    print(backtest_summary(result))
    print(f"Saved {out}")
