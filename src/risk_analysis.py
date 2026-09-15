"""Calculate equity-curve, tail-loss, and drawdown risk metrics."""
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
    df["drawdown_pct"] = np.where(
        df["peak_equity"] != 0,
        df["drawdown"] / df["peak_equity"] * 100,
        0,
    )
    return df


def max_streak(mask):
    best = current = 0
    for value in mask.astype(bool):
        current = current + 1 if value else 0
        best = max(best, current)
    return best


def risk_summary(df):
    x = add_equity_metrics(df)
    pnl = x["pnl"]
    negative = pnl.loc[pnl < 0]
    var_95 = pnl.quantile(0.05)
    tail = pnl.loc[pnl <= var_95]
    max_drawdown = x["drawdown"].min()
    positive = pnl.loc[pnl > 0]
    top_n = max(1, int(np.ceil(len(positive) * 0.10))) if len(positive) else 0
    top_profit_share = (
        positive.nlargest(top_n).sum() / positive.sum() * 100
        if positive.sum() > 0 and top_n
        else 0
    )
    return pd.Series({
        "total_pnl": pnl.sum(),
        "max_drawdown": max_drawdown,
        "max_drawdown_pct": x["drawdown_pct"].min(),
        "pnl_std": pnl.std(),
        "downside_deviation": negative.std() if len(negative) > 1 else 0,
        "trade_level_sharpe_proxy": (pnl.mean() / pnl.std() * np.sqrt(len(pnl))) if pnl.std() else 0,
        "var_95_trade_pnl": var_95,
        "cvar_95_trade_pnl": tail.mean() if len(tail) else var_95,
        "recovery_factor": pnl.sum() / abs(max_drawdown) if max_drawdown < 0 else np.nan,
        "top_10pct_winner_pnl_share_pct": top_profit_share,
        "largest_loss": pnl.min(),
        "largest_win": pnl.max(),
        "max_consecutive_losses": max_streak(pnl < 0),
        "risk_amount_mean": x["risk_amount"].mean(),
    })


if __name__ == "__main__":
    df = pd.read_csv(INPUT, parse_dates=["date"])
    result = risk_summary(df).round(3).to_frame("value")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(OUTPUT)
    print(result)
