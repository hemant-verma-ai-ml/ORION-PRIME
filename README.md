# ⬡ ORION PRIME
### Real-Time Multi-Domain Financial Intelligence OS

> **Built by one person. Designed for institutions. Running on $12/month.**

[![Live System](https://img.shields.io/badge/Status-LIVE-brightgreen)](http://80.225.233.227:3800)
[![Signals](https://img.shields.io/badge/Signals-22M%2B-blue)](http://80.225.233.227:3800)
[![Domains](https://img.shields.io/badge/Domains-4-orange)](http://80.225.233.227:3800)
[![Infrastructure](https://img.shields.io/badge/Cost-%2412%2Fmonth-green)](http://80.225.233.227:3800)

---

## 🎯 What Is ORION PRIME?

ORION PRIME is a production-grade, real-time financial intelligence operating system that ingests, processes, and synthesizes signals across four market domains simultaneously:

| Domain | Status | Signals/Hour | Sources |
|--------|--------|-------------|---------|
| 🔐 **CRYPTO** | ✅ LIVE | ~300,000 | Binance, Futures, Microstructure |
| 🥇 **METALS** | ✅ LIVE | ~5,000 | TwelveData, LME, COT, Backwardation |
| 🛢️ **ENERGY** | ✅ LIVE | ~50 | FRED API, EIA, Shipping |
| 🌍 **MACRO** | 🔄 BUILDING | — | FRED, GDELT, USGS |

**Live dashboard:** [http://80.225.233.227:3800](http://80.225.233.227:3800)

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    ORION PRIME v4.0                      │
├──────────────┬──────────────┬────────────┬──────────────┤
│   CRYPTO     │    METALS    │   ENERGY   │    MACRO     │
│  15 engines  │  12 engines  │  7 collect │  (building)  │
├──────────────┴──────────────┴────────────┴──────────────┤
│              AEGIS-SENSE v4.0 — Signal Bus               │
│         Redis Pub/Sub + TimescaleDB + SQLite Buffer      │
├──────────────────────────────────────────────────────────┤
│       SENTINEL PRIME — Constitutional Governor           │
│    Forensic seal · Integrity mesh · Audit anchoring      │
├──────────────────────────────────────────────────────────┤
│         Oracle Cloud VM + i9 Server (Tailscale VPN)      │
│    Docker · Grafana · FastAPI · Loki · Promtail          │
└──────────────────────────────────────────────────────────┘
```

---

## ⚡ Key Capabilities

### 🔐 Crypto Domain
- **Microstructure Engine** — Order book imbalance, bid/ask depth, spread analysis
- **Cascade Probability Engine** — Liquidation cascade detection and prediction
- **Crypto Pressure Index** — Composite buying/selling pressure across assets
- **Derivatives Intelligence** — Funding rates, open interest, basis monitoring
- **Temporal Pattern Engine** — Time-based regime detection

### 🥇 Metals Domain
- **Backwardation Engine** — Futures curve regime detection across 7 metals
- **COT Smart Money Engine** — CFTC commitment of traders positioning intelligence
- **Industrial Demand Engine** — Bayesian state model for metals consumption
- **Energy-Mining Cost Pressure** — Real-time mining cost vs energy price squeeze
- **Gold Safe Haven Engine** — Cross-asset safe haven demand index

### 🛢️ Energy Domain
- **Oil Collector** — WTI + Brent via FRED API (institutional grade, no IP blocks)
- **Gas Collector** — Henry Hub + Heating Oil via FRED API
- **EIA Collector** — US inventory, production, refinery data
- **Shipping Collector** — Maritime freight rate proxy + chokepoint risk
- **LNG Collector** — Liquefied natural gas netback pricing

### 🌍 Cross-Domain Intelligence
- **Global Crisis Radar** — Multi-domain stress composite
- **Gold vs BTC Safe Haven Ratio** — Real-time safe haven rotation signal
- **Energy vs Mining Squeeze** — Energy cost impact on metals mining margins
- **Liquidity Crisis Composite** — Cross-asset liquidity stress index

---

## 🛡️ SENTINEL PRIME — Constitutional Governor

ORION PRIME runs a sovereign governance layer — SENTINEL PRIME — that enforces deterministic audit controls, forensic sealing, and integrity mesh validation on every decision cycle:

```
🏛️  SENTINEL PRIME: CONSTITUTIONAL GOVERNOR ONLINE
Sovereign Node: Desktop | Integrity: FORENSIC_SEAL_ACTIVE

🔒 SEAL SUCCESS
⚓ ANCHOR: 779671dc17f04dda...
📄 CONTEXT: SRI: 0.10 | Entropy: 0.10 | Reason: Operational Integrity Confirmed. Mesh nominal.
🟢 🛡️ [2026-03-22] PERMIT | Ent: 0.10 | Exp: ₹453,140.32
```

Every signal emitted by ORION carries a cryptographic audit anchor. No signal is acted upon without passing the Sentinel's integrity gate.

---

## 🖥️ ORION COMMAND NODE — Live Telemetry

```
                ORION PRIME — SOVEREIGN COMMAND NODE
┌──────────────────────────────────────────────────────┐
│ NODE ID : 17972006                                    │
│ TOPIC   : orion_sovereign_hemant_2026                 │
│ REDIS   : ONLINE                                      │
└──────────────────────────────────────────────────────┘

  MONETARY MATRIX         SATELLITE TELEMETRY
  ┌───────────┬──────────┐ ┌────────────────────┬────────┐
  │ DXY       │ 100.66   │ │ CARAJAS_BRAZIL     │ ACTIVE │
  │ US10Y     │ 4.48     │ │ NEWMONT_USA        │ ACTIVE │
  │ REGIME    │ VOLATILE │ │ GRASBERG_INDONESIA │ ACTIVE │
  └───────────┴──────────┘ └────────────────────┴────────┘

  MODEL INTEGRITY
  ┌────────┬──────────┐
  │ R²     │ 0.951    │
  │ MAE    │ 0.0023   │
  │ STATUS │ RELIABLE │
  └────────┴──────────┘

  SYSTEM STATUS: STABLE | RISK ENGINE CLEARED
  AUDIT ANCHOR: 7f80763592845d273c89 | NEXT CYCLE: 60s
```

---

## 🛠️ Technology Stack

```yaml
Languages:      Python 3.11, SQL
Databases:      TimescaleDB (PostgreSQL 15), Redis 7, SQLite (buffer)
Infrastructure: Oracle Cloud VM, i9 Home Server, Tailscale VPN
Containers:     Docker, Docker Compose
Monitoring:     Grafana 12.4, Loki, Promtail
API:            FastAPI, asyncpg, aiohttp
Data Sources:   Binance WebSocket, FRED API, TwelveData, EIA, LBMA
Governance:     SENTINEL PRIME — forensic seal, audit anchoring, SRI mesh
```

---

## 📊 Signal Schema

```sql
CREATE TABLE signal_events (
    id          BIGSERIAL PRIMARY KEY,
    created_at  TIMESTAMPTZ DEFAULT NOW(),
    timestamp   TIMESTAMPTZ,
    domain      TEXT,           -- CRYPTO | metals | ENERGY | cross_domain
    asset       TEXT,           -- BTCUSDT | GOLD | WTI | XAU/USD
    source      TEXT,           -- Engine or collector name
    data_type   TEXT,           -- spot_price | cascade_probability | etc.
    value       DOUBLE PRECISION,
    unit        TEXT,
    trust_score REAL,
    metadata    JSONB
);
```

---

## 🏛️ Institutional Design Principles

1. **Fault Tolerance** — SQLite buffer absorbs DB downtime, auto-replays on recovery
2. **Zero Data Loss** — Every signal persisted to TimescaleDB before acknowledgment
3. **Forensic Auditability** — SENTINEL PRIME cryptographic anchoring on every cycle
4. **Observability** — Full log aggregation via Loki + Promtail, Grafana dashboards
5. **Security** — All secrets via environment variables, Tailscale VPN for DB access
6. **Scalability** — Async Python throughout, connection pooling, domain isolation

---

## 📈 Live Metrics (as of March 2026)

- **22M+ signals** ingested and stored
- **300,000+ signals/hour** at peak (crypto domain)
- **29 active signal sources** across all domains
- **4 market domains** running simultaneously
- **$12/month** total infrastructure cost
- **90 days** from zero to production
- **R² = 0.951** model integrity score
- **Zero external capital raised**

---

## 📁 Repository Structure

```
ORION-PRIME/
├── architecture/          # System design diagrams
├── signal_schema/         # Database schema and signal definitions
├── collectors/            # Sample collector implementations
│   ├── crypto/            # Crypto domain collectors
│   ├── metals/            # Metals domain collectors
│   └── energy/            # Energy domain collectors (FRED-based)
├── engines/               # Sample intelligence engine implementations
├── api/                   # FastAPI gateway sample
└── docs/                  # Architecture decisions and documentation
```

---

## 👤 About the Builder

**Hemant Verma** — Quantitative Risk Architect

Ex-Government of India audit. Building institutional-grade financial intelligence systems independently. Market & Model Risk | Governance-first, audit-ready risk systems.

- 📧 hemant.verma866@hotmail.com
- 💼 [linkedin.com/in/hemant-verma-ai-ml-systems](https://www.linkedin.com/in/hemant-verma-ai-ml-systems/)
- 🌐 [Live Dashboard](http://80.225.233.227:3800)

**Open to remote Senior Risk Technology roles globally.**

---

## ⚠️ Note

This repository contains **showcase code only** — architecture samples, signal schemas, and sanitized collector implementations. The production system runs privately with all credentials secured via environment variables.

---

*ORION PRIME — Self-funded. Self-evolving. Built by one person. Designed for billions.*
