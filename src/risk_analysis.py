"""Calculate equity-curve and drawdown risk metrics."""
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "clean_trades.csv"
OUTPUT = ROOT / "reports" / "risk_summary.csv"


def add_equity_metrics(df):
    df = df.sort_values(["date", "trade_id"]).copy()
    df["equity"] = df["pnl"].cumsum()
    df["peak_equity"] = df["equity"].cummax()
    df["drawdown"] = df["equity"] - df["peak_equity"]
    df["drawdown_pct"] = np.where(df["peak_equity"] != 0, df["drawdown"] / df["peak_equity"] * 100, 0)
    return df


def risk_summary(df):
    x = add_equity_metrics(df)
    negative = x.loc[x.pnl < 0, "pnl"]
    return pd.Series({
        "total_pnl": x.pnl.sum(),
        "max_drawdown": x.drawdown.min(),
        "max_drawdown_pct": x.drawdown_pct.min(),
        "pnl_std": x.pnl.std(),
        "downside_deviation": negative.std() if len(negative) > 1 else 0,
        "largest_loss": x.pnl.min(),
        "largest_win": x.pnl.max(),
        "max_consecutive_losses": max_streak(x.pnl < 0),
        "risk_amount_mean": x.risk_amount.mean(),
    })


def max_streak(mask):
    best = current = 0
    for value in mask.astype(bool):
        current = current + 1 if value else 0
        best = max(best, current)
    return best


if __name__ == "__main__":
    df = pd.read_csv(INPUT, parse_dates=["date"])
    result = risk_summary(df).round(3).to_frame("value")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(OUTPUT)
    print(result)
