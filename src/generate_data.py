"""Generate a realistic synthetic trade-level dataset for analytics practice."""
from pathlib import Path
import numpy as np
import pandas as pd

RNG = np.random.default_rng(42)
OUT = Path(__file__).resolve().parents[1] / "data" / "trades.csv"


def generate_trades(n=1200):
    dates = pd.bdate_range("2024-01-02", periods=700)
    strategies = ["Trend Following", "Mean Reversion", "Breakout"]
    instruments = ["XAUUSD", "EURUSD", "GBPUSD", "US100"]
    sessions = ["Asia", "London", "New York"]
    regimes = ["Trending", "Range", "High Volatility"]

    trade_dates = RNG.choice(dates, n)
    strategy = RNG.choice(strategies, n, p=[0.42, 0.33, 0.25])
    instrument = RNG.choice(instruments, n, p=[0.35, 0.25, 0.20, 0.20])
    session = RNG.choice(sessions, n, p=[0.20, 0.42, 0.38])
    regime = RNG.choice(regimes, n, p=[0.42, 0.36, 0.22])

    risk = RNG.uniform(20, 100, n)
    win_prob = np.select(
        [strategy == "Trend Following", strategy == "Mean Reversion"],
        [0.47, 0.57],
        default=0.51,
    )
    wins = RNG.random(n) < win_prob
    rr = RNG.uniform(1.2, 2.8, n)
    gross_pnl = np.where(wins, risk * rr, -risk * RNG.uniform(0.75, 1.05, n))

    # Add modest regime effects so the analysis has meaningful patterns.
    gross_pnl += np.where(regime == "Trending", np.where(wins, 8, 0), 0)
    gross_pnl -= np.where(regime == "High Volatility", RNG.uniform(0, 18, n), 0)

    # Explicit synthetic execution-cost assumptions; these are not broker quotes.
    spread_cost = RNG.uniform(0.5, 2.5, n)
    slippage_cost = RNG.uniform(0.2, 1.5, n)
    commission = RNG.uniform(0.5, 2.0, n)
    total_cost = spread_cost + slippage_cost + commission
    net_pnl = gross_pnl - total_cost

    df = pd.DataFrame({
        "trade_id": np.arange(1, n + 1),
        "date": trade_dates,
        "strategy": strategy,
        "instrument": instrument,
        "session": session,
        "market_regime": regime,
        "risk_amount": risk.round(2),
        "gross_pnl": gross_pnl.round(2),
        "spread_cost": spread_cost.round(2),
        "slippage_cost": slippage_cost.round(2),
        "commission": commission.round(2),
        "pnl": net_pnl.round(2),
    }).sort_values("date")
    df["total_cost"] = (df["gross_pnl"] - df["pnl"]).round(2)
    df["return_on_risk_pct"] = (df["pnl"] / df["risk_amount"] * 100).round(2)
    df["outcome"] = np.where(df["pnl"] > 0, "Win", "Loss")
    return df.reset_index(drop=True)


if __name__ == "__main__":
    OUT.parent.mkdir(parents=True, exist_ok=True)
    generate_trades().to_csv(OUT, index=False)
    print(f"Generated {OUT}")
