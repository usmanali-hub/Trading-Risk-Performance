import pandas as pd
import pytest

from src.backtest import backtest_summary, moving_average_backtest


def sample_market():
    return pd.DataFrame(
        {
            "date": pd.date_range("2025-01-01", periods=8, freq="D"),
            "close": [100, 101, 102, 103, 104, 103, 105, 106],
        }
    )


def test_backtest_requires_fast_window_below_slow_window():
    with pytest.raises(ValueError):
        moving_average_backtest(sample_market(), fast_window=10, slow_window=5)


def test_signal_is_lagged_to_avoid_same_close_lookahead():
    result = moving_average_backtest(sample_market(), fast_window=2, slow_window=3)
    first_valid = result["slow_ma"].first_valid_index()
    assert result.loc[first_valid, "position"] == 0
    assert result["position"].iloc[-1] in (-1, 1)


def test_costs_reduce_gross_pnl_when_trading_occurs():
    result = moving_average_backtest(sample_market(), fast_window=2, slow_window=3)
    summary = backtest_summary(result)
    assert summary["total_costs"] >= 0
    assert summary["net_pnl"] <= summary["gross_pnl"]
