-- Trading Risk & Performance Analytics
-- Assumes a table named trades with the columns in data/trades.csv.

-- 1. Overall performance
SELECT
    COUNT(*) AS trades,
    ROUND(SUM(pnl), 2) AS total_pnl,
    ROUND(100.0 * AVG(CASE WHEN pnl > 0 THEN 1.0 ELSE 0.0 END), 2) AS win_rate_pct,
    ROUND(AVG(pnl), 2) AS avg_trade_pnl,
    ROUND(SUM(CASE WHEN pnl > 0 THEN pnl ELSE 0 END)
        / NULLIF(ABS(SUM(CASE WHEN pnl < 0 THEN pnl ELSE 0 END)), 0), 2) AS profit_factor
FROM trades;

-- 2. Performance by strategy
SELECT
    strategy,
    COUNT(*) AS trades,
    ROUND(SUM(pnl), 2) AS total_pnl,
    ROUND(100.0 * AVG(CASE WHEN pnl > 0 THEN 1.0 ELSE 0.0 END), 2) AS win_rate_pct,
    ROUND(AVG(pnl), 2) AS expectancy
FROM trades
GROUP BY strategy
ORDER BY total_pnl DESC;

-- 3. Instrument contribution
SELECT
    instrument,
    COUNT(*) AS trades,
    ROUND(SUM(pnl), 2) AS total_pnl,
    ROUND(AVG(return_on_risk_pct), 2) AS avg_return_on_risk_pct
FROM trades
GROUP BY instrument
ORDER BY total_pnl DESC;

-- 4. Session analysis
SELECT
    session,
    COUNT(*) AS trades,
    ROUND(SUM(pnl), 2) AS total_pnl,
    ROUND(AVG(pnl), 2) AS avg_pnl
FROM trades
GROUP BY session
ORDER BY avg_pnl DESC;

-- 5. Market-regime analysis
SELECT
    market_regime,
    COUNT(*) AS trades,
    ROUND(SUM(pnl), 2) AS total_pnl,
    ROUND(100.0 * AVG(CASE WHEN pnl > 0 THEN 1.0 ELSE 0.0 END), 2) AS win_rate_pct
FROM trades
GROUP BY market_regime
ORDER BY total_pnl DESC;

-- 6. Monthly performance
SELECT
    DATE_TRUNC('month', date) AS month,
    COUNT(*) AS trades,
    ROUND(SUM(pnl), 2) AS total_pnl
FROM trades
GROUP BY DATE_TRUNC('month', date)
ORDER BY month;
