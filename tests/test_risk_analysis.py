import pandas as pd

from src.risk_analysis import add_equity_metrics, max_streak, risk_summary


def sample_trades():
    return pd.DataFrame({
        "trade_id": [1, 2, 3, 4],
        "date": pd.to_datetime(["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04"]),
        "pnl": [100.0, -50.0, -25.0, 75.0],
        "risk_amount": [100.0] * 4,
    })


def test_max_streak():
    assert max_streak(pd.Series([False, True, True, False, True])) == 2


def test_equity_metrics():
    result = add_equity_metrics(sample_trades())
    assert result["equity"].tolist() == [100.0, 50.0, 25.0, 100.0]
    assert result["drawdown"].min() == -75.0


def test_risk_summary_contains_tail_metrics():
    result = risk_summary(sample_trades())
    assert result["total_pnl"] == 100.0
    assert "var_95_trade_pnl" in result
    assert "cvar_95_trade_pnl" in result
    assert "recovery_factor" in result
