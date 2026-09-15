"""Validate and clean the synthetic trade dataset."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "trades.csv"
OUTPUT = ROOT / "data" / "clean_trades.csv"
REQUIRED = ["trade_id", "date", "strategy", "instrument", "session", "market_regime", "risk_amount", "pnl", "return_on_risk_pct", "outcome"]


def clean(df):
    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    numeric = ["risk_amount", "pnl", "return_on_risk_pct"]
    for col in numeric:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=REQUIRED)
    df = df.drop_duplicates(subset="trade_id")
    df = df[df["risk_amount"] > 0]
    df["outcome"] = df["pnl"].gt(0).map({True: "Win", False: "Loss"})
    return df.sort_values(["date", "trade_id"]).reset_index(drop=True)


if __name__ == "__main__":
    df = pd.read_csv(INPUT)
    cleaned = clean(df)
    cleaned.to_csv(OUTPUT, index=False)
    print(f"Validated {len(cleaned):,} trades and saved {OUTPUT}")
