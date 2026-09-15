"""Interactive dashboard for Trading Risk & Performance Analytics."""
from pathlib import Path
import subprocess
import sys

import pandas as pd
import streamlit as st

from src.backtest import backtest_summary, moving_average_backtest
from src.market_data import download_daily
from src.risk_analysis import risk_summary

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "clean_trades.csv"

st.set_page_config(page_title="Trading Risk & Performance", layout="wide")
st.title("Trading Risk & Performance Analytics")
st.caption("Trade-level risk analytics plus an optional historical Forex validation path. Synthetic results are clearly separated from public-market backtest results.")


def prepare_data():
    needs_refresh = not DATA.exists()
    if DATA.exists():
        try:
            needs_refresh = "gross_pnl" not in pd.read_csv(DATA, nrows=1).columns
        except Exception:
            needs_refresh = True
    if needs_refresh:
        subprocess.run([sys.executable, "src/generate_data.py"], cwd=ROOT, check=True)
        subprocess.run([sys.executable, "src/clean_data.py"], cwd=ROOT, check=True)


try:
    prepare_data()
    df = pd.read_csv(DATA, parse_dates=["date"])
except Exception as exc:
    st.error(f"Could not prepare the dataset: {exc}")
    st.stop()

with st.sidebar:
    st.header("Synthetic filters")
    strategies = st.multiselect("Strategy", sorted(df["strategy"].unique()), default=sorted(df["strategy"].unique()))
    regimes = st.multiselect("Market regime", sorted(df["market_regime"].unique()), default=sorted(df["market_regime"].unique()))

filtered = df[df["strategy"].isin(strategies) & df["market_regime"].isin(regimes)].copy()
if filtered.empty:
    st.warning("No trades match the selected filters.")
    st.stop()

risk = risk_summary(filtered)
gross_pnl = filtered["gross_pnl"].sum()
total_cost = filtered["total_cost"].sum()
wins = filtered.loc[filtered.pnl > 0, "pnl"].sum()
losses = abs(filtered.loc[filtered.pnl < 0, "pnl"].sum())
profit_factor = wins / losses if losses else float("inf")

st.subheader("Executive Risk Panel — Synthetic Trade Dataset")
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Net P&L", f"{filtered.pnl.sum():,.2f}")
c2.metric("Max Drawdown", f"{risk['max_drawdown']:,.2f}")
c3.metric("Profit Factor", f"{profit_factor:.2f}")
c4.metric("CVaR 95%", f"{risk['cvar_95_trade_pnl']:,.2f}")
c5.metric("Recovery Factor", f"{risk['recovery_factor']:.2f}" if pd.notna(risk['recovery_factor']) else "N/A")

c1, c2, c3 = st.columns(3)
c1.metric("Trades", f"{len(filtered):,}")
c2.metric("Net Win Rate", f"{filtered.pnl.gt(0).mean()*100:.1f}%")
c3.metric("Execution Costs", f"{total_cost:,.2f}", delta=f"Gross {gross_pnl:,.2f}")

left, right = st.columns(2)
with left:
    st.subheader("Net Equity Curve")
    equity = filtered.sort_values(["date", "trade_id"]).assign(equity=lambda x: x.pnl.cumsum())
    st.line_chart(equity.set_index("date")["equity"])
with right:
    st.subheader("Drawdown Curve")
    equity["peak"] = equity["equity"].cummax()
    equity["drawdown"] = equity["equity"] - equity["peak"]
    st.line_chart(equity.set_index("date")["drawdown"])

left, right = st.columns(2)
with left:
    st.subheader("P&L by Strategy")
    st.bar_chart(filtered.groupby("strategy")["pnl"].sum().sort_values())
with right:
    st.subheader("Average P&L by Market Regime")
    st.bar_chart(filtered.groupby("market_regime")["pnl"].mean().sort_values())

st.subheader("Performance by Market Regime")
regime = filtered.groupby("market_regime")["pnl"].agg(["count", "sum", "mean"]).round(2)
st.dataframe(regime, use_container_width=True)

st.subheader("Execution Cost Breakdown")
costs = filtered[["spread_cost", "slippage_cost", "commission"]].sum().round(2)
st.dataframe(costs.rename("cost").to_frame(), use_container_width=True)

st.subheader("Historical Forex Validation")
st.write("This optional path downloads public daily market data and runs a simple moving-average strategy with explicit spread, slippage, and commission assumptions. It is a validation demonstration, not broker performance or investment advice.")

with st.expander("Backtest assumptions"):
    col1, col2, col3 = st.columns(3)
    fast = col1.number_input("Fast MA", min_value=5, max_value=100, value=20)
    slow = col2.number_input("Slow MA", min_value=10, max_value=250, value=50)
    units = col3.number_input("Units", min_value=1_000, max_value=100_000, value=10_000, step=1_000)
    col1, col2, col3 = st.columns(3)
    spread_bps = col1.number_input("Spread (bps)", min_value=0.0, max_value=20.0, value=1.0, step=0.1)
    slippage_bps = col2.number_input("Slippage (bps)", min_value=0.0, max_value=20.0, value=0.5, step=0.1)
    commission = col3.number_input("Commission / 100k", min_value=0.0, max_value=50.0, value=7.0, step=1.0)

if st.button("Run EURUSD historical validation"):
    try:
        market = download_daily("EURUSD", start="2020-01-01")
        result = moving_average_backtest(market, fast_window=fast, slow_window=slow, units=units, spread_bps=spread_bps, slippage_bps=slippage_bps, commission_per_100k=commission)
        summary = backtest_summary(result)
        a, b, c, d = st.columns(4)
        a.metric("Gross P&L", f"{summary['gross_pnl']:,.2f}")
        b.metric("Net P&L", f"{summary['net_pnl']:,.2f}")
        c.metric("Total Costs", f"{summary['total_costs']:,.2f}")
        d.metric("Max Net Drawdown", f"{summary['max_net_drawdown']:,.2f}")
        st.line_chart(result.set_index("date")[["equity_gross", "equity_net"]])
        st.dataframe(result.tail(20), use_container_width=True)
        st.caption("Public historical market data is used only to validate the analytics pipeline. Strategy parameters and execution costs are assumptions and should not be interpreted as evidence of future returns.")
    except Exception as exc:
        st.error(f"Historical validation could not be completed: {exc}")

st.subheader("Risk Notes")
st.info("The core portfolio dataset is synthetic and fixed-seed. Its metrics are analytical demonstrations. The historical validation path uses public market data and explicit assumptions, but it is still a simplified backtest rather than a live execution system.")
