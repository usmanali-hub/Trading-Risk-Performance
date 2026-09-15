"""Calculate core trading performance metrics and segment results."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "clean_trades.csv"
OUTPUT = ROOT / "reports" / "performance_summary.csv"


def metrics(df):
    wins = df.loc[df.pnl > 0, "pnl"]
    losses = df.loc[df.pnl < 0, "pnl"]
    gross_profit = wins.sum()
    gross_loss = abs(losses.sum())
    return pd.Series({
        "trades": len(df),
        "total_pnl": df.pnl.sum(),
        "win_rate_pct": (df.pnl.gt(0).mean() * 100),
        "avg_trade_pnl": df.pnl.mean(),
        "avg_win": wins.mean() if len(wins) else 0,
        "avg_loss": losses.mean() if len(losses) else 0,
        "profit_factor": gross_profit / gross_loss if gross_loss else float("inf"),
        "expectancy": df.pnl.mean(),
        "avg_return_on_risk_pct": df.return_on_risk_pct.mean(),
    })


def segmented(df):
    frames = []
    for dimension in ["strategy", "instrument", "session", "market_regime"]:
        part = df.groupby(dimension).apply(metrics, include_groups=False).reset_index()
        part.insert(0, "dimension", dimension)
        part = part.rename(columns={dimension: "segment"})
        frames.append(part)
    return pd.concat(frames, ignore_index=True)


if __name__ == "__main__":
    df = pd.read_csv(INPUT, parse_dates=["date"])
    summary = segmented(df).round(3)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(OUTPUT, index=False)
    print(summary.to_string(index=False))
