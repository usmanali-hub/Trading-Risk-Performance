import pytest

from src.exposure_risk import (
    exposure_pct,
    leverage_ratio,
    margin_requirement,
    notional_exposure,
    position_size,
    risk_amount,
    within_exposure_limit,
)


def test_risk_amount_and_position_size():
    risk = risk_amount(10_000, 1.0)
    assert risk == pytest.approx(100.0)
    assert position_size(risk, 0.005, 1.0) == pytest.approx(20_000.0)


def test_notional_margin_and_exposure():
    notional = notional_exposure(10_000, 1.25)
    assert notional == pytest.approx(12_500.0)
    assert margin_requirement(notional, 50) == pytest.approx(250.0)
    assert exposure_pct(notional, 10_000) == pytest.approx(125.0)
    assert leverage_ratio(notional, 10_000) == pytest.approx(1.25)


def test_exposure_limit():
    assert within_exposure_limit(5_000, 10_000, 50.0)
    assert not within_exposure_limit(5_001, 10_000, 50.0)


@pytest.mark.parametrize(
    "fn,args",
    [
        (risk_amount, (0, 1)),
        (risk_amount, (10_000, -1)),
        (position_size, (100, 0, 1)),
        (position_size, (100, 1, 0)),
        (notional_exposure, (1, 0)),
        (notional_exposure, (-1, 100)),
        (margin_requirement, (100, 0)),
        (exposure_pct, (100, 0)),
        (leverage_ratio, (100, 0)),
        (within_exposure_limit, (100, 10_000, -1)),
    ],
)
def test_invalid_inputs_raise(fn, args):
    with pytest.raises(ValueError):
        fn(*args)
