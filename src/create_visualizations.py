"""Create portfolio-ready SVG charts from the cleaned trade dataset."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "clean_trades.csv"
OUT = ROOT / "visualizations"


def save_charts(df):
    OUT.mkdir(parents=True, exist_ok=True)
    x = df.sort_values(["date", "trade_id"]).copy()
    x["equity"] = x["pnl"].cumsum()
    x["peak"] = x["equity"].cummax()
    x["drawdown"] = x["equity"] - x["peak"]

    plt.figure(figsize=(11, 5)); plt.plot(x["date"], x["equity"]); plt.title("Cumulative Trading P&L"); plt.xlabel("Date"); plt.ylabel("Cumulative P&L"); plt.tight_layout(); plt.savefig(OUT / "equity_curve.svg", format="svg"); plt.close()
    plt.figure(figsize=(11, 5)); plt.fill_between(x["date"], x["drawdown"], 0); plt.title("Trading Drawdown"); plt.xlabel("Date"); plt.ylabel("Drawdown"); plt.tight_layout(); plt.savefig(OUT / "drawdown.svg", format="svg"); plt.close()
    strategy = x.groupby("strategy")["pnl"].sum().sort_values(); plt.figure(figsize=(9, 5)); strategy.plot(kind="barh"); plt.title("Total P&L by Strategy"); plt.xlabel("Total P&L"); plt.tight_layout(); plt.savefig(OUT / "strategy_pnl.svg", format="svg"); plt.close()
    regime = x.groupby("market_regime")["pnl"].mean().sort_values(); plt.figure(figsize=(9, 5)); regime.plot(kind="barh"); plt.title("Average P&L by Market Regime"); plt.xlabel("Average P&L per Trade"); plt.tight_layout(); plt.savefig(OUT / "regime_avg_pnl.svg", format="svg"); plt.close()


if __name__ == "__main__":
    save_charts(pd.read_csv(INPUT, parse_dates=["date"]))
    print(f"Charts saved to {OUT}")
