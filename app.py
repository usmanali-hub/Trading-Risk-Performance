"""Interactive dashboard for Trading Risk & Performance Analytics."""
from pathlib import Path
import subprocess
import sys

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "clean_trades.csv"

st.set_page_config(page_title="Trading Risk & Performance", layout="wide")
st.title("Trading Risk & Performance Analytics")
st.caption("Interactive portfolio dashboard using the project's fixed-seed synthetic trade data.")


def prepare_data():
    if not DATA.exists():
        subprocess.run([sys.executable, "src/generate_data.py"], cwd=ROOT, check=True)
        subprocess.run([sys.executable, "src/clean_data.py"], cwd=ROOT, check=True)


try:
    prepare_data()
    df = pd.read_csv(DATA, parse_dates=["date"])
except Exception as exc:
    st.error(f"Could not prepare the dataset: {exc}")
    st.stop()

with st.sidebar:
    st.header("Filters")
    strategies = st.multiselect("Strategy", sorted(df["strategy"].unique()), default=sorted(df["strategy"].unique()))
    regimes = st.multiselect("Market regime", sorted(df["market_regime"].unique()), default=sorted(df["market_regime"].unique()))

filtered = df[df["strategy"].isin(strategies) & df["market_regime"].isin(regimes)].copy()

wins = filtered.loc[filtered.pnl > 0, "pnl"]
losses = filtered.loc[filtered.pnl < 0, "pnl"]
gross_loss = abs(losses.sum())
profit_factor = wins.sum() / gross_loss if gross_loss else float("inf")

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Trades", f"{len(filtered):,}")
c2.metric("Total P&L", f"{filtered.pnl.sum():,.2f}")
c3.metric("Win Rate", f"{filtered.pnl.gt(0).mean()*100:.1f}%")
c4.metric("Profit Factor", f"{profit_factor:.2f}")
c5.metric("Avg Trade", f"{filtered.pnl.mean():,.2f}")

left, right = st.columns(2)
with left:
    st.subheader("Equity Curve")
    equity = filtered.sort_values("date").assign(equity=lambda x: x.pnl.cumsum())
    st.line_chart(equity.set_index("date")["equity"])
with right:
    st.subheader("P&L by Strategy")
    strategy_pnl = filtered.groupby("strategy")["pnl"].sum().sort_values()
    st.bar_chart(strategy_pnl)

st.subheader("Performance by Market Regime")
regime = filtered.groupby("market_regime")["pnl"].agg(["count", "sum", "mean"]).round(2)
st.dataframe(regime, use_container_width=True)

st.subheader("Risk Notes")
st.info("The dataset is synthetic and fixed-seed. Metrics are analytical demonstrations, not investment advice or evidence of future performance.")
