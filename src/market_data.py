"""Download public historical market data for reproducible backtests.

The downloader uses Yahoo Finance's public chart endpoint and writes raw OHLCV
observations locally. It is an optional validation path; the portfolio's core
synthetic dataset remains fixed-seed and reproducible without network access.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import urllib.parse
import urllib.request

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "data" / "market" / "eurusd_daily.csv"

TICKERS = {
    "EURUSD": "EURUSD=X",
    "XAUUSD": "XAUUSD=X",
}


def download_daily(symbol="EURUSD", start="2020-01-01", end=None, output=None):
    """Download daily OHLC data for a public Yahoo Finance ticker."""
    ticker = TICKERS.get(symbol.upper(), symbol)
    start_dt = datetime.fromisoformat(start).replace(tzinfo=timezone.utc)
    end_dt = (
        datetime.fromisoformat(end).replace(tzinfo=timezone.utc)
        if end
        else datetime.now(timezone.utc)
    )
    params = urllib.parse.urlencode(
        {
            "period1": int(start_dt.timestamp()),
            "period2": int(end_dt.timestamp()),
            "interval": "1d",
            "events": "history",
            "includeAdjustedClose": "true",
        }
    )
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(ticker)}?{params}"
    with urllib.request.urlopen(url, timeout=30) as response:
        payload = json.load(response)

    result = payload["chart"]["result"][0]
    timestamps = result.get("timestamp", [])
    quote = result["indicators"]["quote"][0]
    frame = pd.DataFrame(quote, index=pd.to_datetime(timestamps, unit="s", utc=True))
    frame.index = frame.index.tz_convert(None).normalize()
    frame = frame.rename_axis("date").reset_index()
    frame["symbol"] = symbol.upper()
    frame = frame[["date", "symbol", "open", "high", "low", "close", "volume"]]
    frame = frame.dropna(subset=["open", "high", "low", "close"]).drop_duplicates("date")

    target = Path(output) if output else ROOT / "data" / "market" / f"{symbol.lower()}_daily.csv"
    target.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(target, index=False)
    return frame


if __name__ == "__main__":
    frame = download_daily()
    print(f"Downloaded {len(frame):,} EURUSD observations to {DEFAULT_OUT}")
