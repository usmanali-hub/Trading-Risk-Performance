"""Generic position-sizing and exposure-risk calculations.

These formulas are intentionally broker-agnostic. They provide a transparent
risk-control layer for portfolio analysis; they are not a substitute for a
broker's instrument specifications, currency conversion rules, or margin
engine.
"""


def risk_amount(account_equity: float, risk_pct: float) -> float:
    """Return the currency amount allowed at risk for one trade."""
    if account_equity <= 0:
        raise ValueError("account_equity must be greater than zero")
    if risk_pct < 0:
        raise ValueError("risk_pct must be non-negative")
    return account_equity * risk_pct / 100.0


def position_size(
    risk_amount_value: float,
    stop_distance: float,
    value_per_unit: float,
) -> float:
    """Calculate units from risk budget, stop distance, and unit value."""
    if risk_amount_value < 0:
        raise ValueError("risk_amount_value must be non-negative")
    if stop_distance <= 0:
        raise ValueError("stop_distance must be greater than zero")
    if value_per_unit <= 0:
        raise ValueError("value_per_unit must be greater than zero")
    return risk_amount_value / (stop_distance * value_per_unit)


def notional_exposure(
    units: float,
    price: float,
    contract_size: float = 1.0,
) -> float:
    """Return simplified market-value notional exposure."""
    if units < 0:
        raise ValueError("units must be non-negative")
    if price <= 0:
        raise ValueError("price must be greater than zero")
    if contract_size <= 0:
        raise ValueError("contract_size must be greater than zero")
    return units * price * contract_size


def margin_requirement(notional: float, leverage: float) -> float:
    """Return simplified margin requirement as notional divided by leverage."""
    if notional < 0:
        raise ValueError("notional must be non-negative")
    if leverage <= 0:
        raise ValueError("leverage must be greater than zero")
    return notional / leverage


def exposure_pct(notional: float, account_equity: float) -> float:
    """Return notional exposure as a percentage of account equity."""
    if notional < 0:
        raise ValueError("notional must be non-negative")
    if account_equity <= 0:
        raise ValueError("account_equity must be greater than zero")
    return notional / account_equity * 100.0


def leverage_ratio(notional: float, account_equity: float) -> float:
    """Return gross notional divided by account equity."""
    if notional < 0:
        raise ValueError("notional must be non-negative")
    if account_equity <= 0:
        raise ValueError("account_equity must be greater than zero")
    return notional / account_equity


def within_exposure_limit(
    notional: float,
    account_equity: float,
    max_exposure_pct: float,
) -> bool:
    """Check whether notional exposure stays within a configured limit."""
    if max_exposure_pct < 0:
        raise ValueError("max_exposure_pct must be non-negative")
    return exposure_pct(notional, account_equity) <= max_exposure_pct
