-- ORION PRIME — Signal Events Schema
-- TimescaleDB hypertable for time-series signal storage

CREATE TABLE signal_events (
    id          BIGSERIAL PRIMARY KEY,
    created_at  TIMESTAMPTZ DEFAULT NOW(),
    timestamp   TIMESTAMPTZ,
    domain      TEXT NOT NULL,
    asset       TEXT NOT NULL,
    source      TEXT NOT NULL,
    data_type   TEXT NOT NULL,
    value       DOUBLE PRECISION NOT NULL,
    unit        TEXT,
    trust_score REAL DEFAULT 0.5,
    metadata    JSONB DEFAULT '{}'
);

-- Convert to TimescaleDB hypertable
SELECT create_hypertable('signal_events', 'created_at');

-- Indexes for query performance
CREATE INDEX idx_signal_asset_source ON signal_events(asset, source, data_type);
CREATE INDEX idx_signal_domain ON signal_events(domain, created_at DESC);
CREATE INDEX idx_signal_created ON signal_events(created_at DESC);

-- Sample domains
-- CRYPTO       : binance spot, futures, microstructure engines
-- metals       : TwelveData, backwardation, COT, industrial demand
-- ENERGY       : FRED API (WTI, Brent, NatGas), EIA, shipping
-- cross_domain : crisis radar, safe haven ratio, liquidity composite

-- Sample data types by domain
-- CRYPTO  : spot_price, futures_price, funding_rate, open_interest,
--           order_book_imbalance, cascade_probability_index,
--           crypto_pressure_index, microstructure_pressure
-- metals  : spot_price, backwardation_intensity, futures_curve_regime,
--           cot_smart_money_index, cot_regime_signal,
--           industrial_demand_index, energy_mining_cost_pressure
-- ENERGY  : SPOT_PRICE, SPREAD, SENTIMENT_SCORE, FREIGHT_RATE_PROXY
-- cross   : global_crisis_radar, gold_vs_btc_safe_haven_ratio,
--           energy_vs_mining_squeeze, liquidity_crisis_composite
