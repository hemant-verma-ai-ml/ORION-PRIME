# ⚡ ORION PRIME — Real-Time Financial Intelligence Platform

<div align="center">

[![Status](https://img.shields.io/badge/Status-LIVE%20PRODUCTION-brightgreen?style=for-the-badge)](/)
[![Signals](https://img.shields.io/badge/Signals%20Ingested-14.1M%2B-blue?style=for-the-badge)](/)
[![Throughput](https://img.shields.io/badge/Throughput-13%2C800%2Fmin-orange?style=for-the-badge)](/)
[![Engines](https://img.shields.io/badge/Active%20Engines-28%2B-purple?style=for-the-badge)](/)
[![Uptime](https://img.shields.io/badge/Uptime-24%2F7-success?style=for-the-badge)](/)

**A production-grade, distributed financial signal intelligence system built entirely from scratch.**
Ingests, processes, and serves real-time market signals across Crypto, Metals, and Energy domains
through a self-healing async engine mesh — deployed on cloud infrastructure.

</div>

---

## What This Project Demonstrates

This is a solo-built, end-to-end distributed systems project running live in production.

| Capability | Detail |
|---|---|
| **Distributed Systems** | 6-container Docker mesh, async Python engine orchestration, Redis pub/sub event bus |
| **Data Engineering** | 13,800 signals/min sustained ingestion, TimescaleDB hypertables, JSONB metadata |
| **Backend Engineering** | FastAPI + JWT auth + rate limiting, WebSocket streaming, REST API |
| **DevOps / Cloud** | Oracle Cloud ARM deployment, Nginx reverse proxy, SSL, multi-environment Docker Compose |
| **AI Integration** | Local LLM (Qwen2.5-Coder-7B via Ollama) powering autonomous debugging agent |
| **Observability** | Grafana War Room, structured JSON logging, engine heartbeat telemetry |
| **System Design** | Event-driven architecture, self-healing watchdog, domain-isolated engine registry |

---

## Live System Metrics

```
┌─────────────────────────────────────────────────────┐
│           SOVEREIGN MEMORY — DB Stats               │
│                                                     │
│   Total Signals    │  14,141,926                    │
│   Last 5 Min       │  76,390                        │
│   Active Engines   │  18                            │
│   Avg Trust Score  │  0.976                         │
└─────────────────────────────────────────────────────┘
```

*Screenshot taken from live Grafana dashboard — March 2026*

---

## System Architecture

```
                        ┌─────────────────────────────┐
                        │      DATA SOURCES           │
                        │                             │
                        │  Binance WebSocket (live)   │
                        │  Bybit WebSocket (live)     │
                        │  MCX India REST             │
                        │  COMEX / LME feeds          │
                        │  FRED API (macro)           │
                        │  EIA API (energy)           │
                        │  CFTC COT reports           │
                        └──────────────┬──────────────┘
                                       │
                        ┌──────────────▼──────────────┐
                        │   AEGIS-SENSE ENGINE MESH   │
                        │                             │
                        │  28+ async Python engines   │
                        │  EventRateMixin pattern     │
                        │  Auto-discovery registry    │
                        │  Per-engine heartbeat       │
                        └──────────────┬──────────────┘
                                       │
                        ┌──────────────▼──────────────┐
                        │      REDIS EVENT BUS        │
                        │   AEGIS_SIGNAL_BUS channel  │
                        │   AOF persistent, 400MB     │
                        └──────────────┬──────────────┘
                                       │
                        ┌──────────────▼──────────────┐
                        │   TIMESCALEDB STORAGE       │
                        │   signal_events hypertable  │
                        │   14.1M+ rows, BRIN indexes │
                        │   JSONB metadata per signal │
                        └──────────────┬──────────────┘
                                       │
               ┌───────────────────────┼───────────────────────┐
               │                       │                       │
┌──────────────▼──────┐  ┌─────────────▼──────┐  ┌────────────▼──────────┐
│   FastAPI Gateway   │  │  Grafana War Room  │  │   WebSocket Stream   │
│   JWT + Rate Limit  │  │  Live dashboards   │  │   Real-time signals  │
│   Port 8100         │  │  Port 3800         │  │   /ws/signals        │
└─────────────────────┘  └────────────────────┘  └──────────────────────┘
```

---

## Tech Stack

### Core Infrastructure
| Technology | Version | Role |
|---|---|---|
| **Python** | 3.11 | Async engine mesh, all business logic |
| **asyncio** | stdlib | Concurrent engine orchestration |
| **TimescaleDB** | PostgreSQL 15 | Time-series signal storage + hypertables |
| **Redis** | 7-Alpine | Async pub/sub event bus (AOF persistent) |
| **FastAPI** | Latest | REST API + WebSocket gateway |
| **Docker** | 29.3.0 | Container orchestration |
| **Docker Compose** | v5.1.0 | Multi-service deployment |
| **Grafana** | Latest | Real-time observability dashboards |

### Cloud & DevOps
| Technology | Role |
|---|---|
| **Oracle Cloud ARM** (Ampere A1) | Production VM — Ubuntu 22.04 LTS, aarch64 |
| **Nginx** | Reverse proxy + SSL termination |
| **Let's Encrypt** | Automated SSL certificates |
| **Tailscale VPN** | Secure private tunnel between nodes |
| **asyncpg** | High-performance async PostgreSQL driver |
| **uvicorn** | ASGI server for FastAPI |

### AI & Intelligence
| Technology | Role |
|---|---|
| **Ollama** | Local LLM inference server |
| **Qwen2.5-Coder-7B** | Code generation + autonomous debugging |
| **Custom NLP pipeline** | Signal interpretation in plain English |

### Python Libraries
```
asyncio · asyncpg · redis.asyncio · fastapi · uvicorn · pydantic
websockets · aiohttp · pandas · numpy · scipy · dataclasses
python-jose (JWT) · structlog · prometheus-client · httpx
```

---

## Domain Intelligence

### Crypto Domain ✅ Live
Real-time microstructure intelligence on BTC, ETH, SOL, BNB, XRP, DOGE.

```python
# Example signal output
{
  "asset": "BTCUSDT",
  "source": "MicrostructureEngine",
  "data_type": "order_book_imbalance",
  "value": -0.2254,
  "unit": "ratio",
  "domain": "CRYPTO",
  "trust_score": 0.98,
  "timestamp": "2026-03-15T11:39:35.846642+00:00"
}
```

**Engines:** SpotEngine · FuturesEngine · FundingEngine · OpenInterestEngine
· MicrostructureEngine · LiquidationCascadeEngine · CryptoPressureIndex
· OnChainController · TemporalPatternEngine · AnomalyEngine

**Throughput:** 4,800+ events/min from MicrostructureEngine alone

### Metals Domain ✅ Live
Physical + paper market intelligence with 15 active engines.

**Engines:** MCXCollector · BackwardationEngine · PhysicalPremiumEngine
· CrossMetalRatioEngine · MiningCostEngine · BayesianDemandModel
· COTSmartMoneyEngine · EnergyMetalCouplingEngine · MetalsPressureIndex

**Assets:** Gold ($2.70K) · Silver · Copper ($2.22) · Nickel · Platinum · Palladium · Aluminium

### Energy Domain ⏳ Building
Oil · Natural Gas · Coal with EIA inventory signals.

---

## Dev AI — Autonomous Debug System

An embedded AI development assistant that monitors, diagnoses, and proposes fixes autonomously.

```
dev_ai/
├── debugger/
│   ├── autonomous_debug_agent.py  # Orchestrates full debug cycle
│   ├── error_detector.py          # AST + log pattern scanning
│   ├── fix_generator.py           # LLM-powered fix proposals
│   ├── patch_engine.py            # Validated patch application
│   └── log_analyzer.py            # Multi-source log ingestion
├── validators/                    # 8-layer validation before any patch
│   ├── syntax_validator.py
│   ├── import_validator.py
│   ├── security_validator.py
│   └── architecture_validator.py
└── telegram/                      # Remote control interface
    ├── telegram_bot.py            # /debug /approve /reject /status
    └── approval_manager.py        # Human-in-the-loop gate
```

**How it works:**
1. Scans project logs every 5 minutes autonomously
2. Detects errors via AST analysis + pattern matching
3. Sends error context to local Qwen2.5-Coder-7B LLM
4. Generated fix passes 8-layer validation pipeline
5. Proposes patch via Telegram — requires human `/approve`
6. Zero auto-apply — all changes are human-gated

**Telegram bot live:** `/status /scan /debug /generate /approve /reject /logs /pending`

---

## Signal Schema

Unified schema across all domains — zero schema changes as new domains are added:

```sql
CREATE TABLE signal_events (
    id          BIGSERIAL PRIMARY KEY,
    domain      VARCHAR(50)  NOT NULL,     -- CRYPTO | metals | energy
    asset       VARCHAR(50),               -- BTCUSDT | GOLD | WTI
    source      VARCHAR(100),              -- engine name
    data_type   VARCHAR(100) NOT NULL,     -- signal type
    value       DOUBLE PRECISION NOT NULL, -- normalized value
    unit        VARCHAR(50),               -- ratio | USD | contracts
    timestamp   TIMESTAMPTZ NOT NULL,      -- UTC, indexed
    trust_score DOUBLE PRECISION,          -- source reliability 0-1
    metadata    JSONB                      -- engine-specific context
);

-- TimescaleDB hypertable — automatic time-based partitioning
SELECT create_hypertable('signal_events', 'timestamp');
```

**Indexes:** BRIN on timestamp · btree on (asset, data_type) · GIN on metadata JSONB

---

## Deployment

### Cloud Infrastructure

```
Oracle Cloud ARM (Ampere A1 Flex)
├── Shape:    VM.Standard.A1.Flex
├── OCPU:     4 (scalable to 12 — Always Free)
├── RAM:      24 GB
├── Storage:  50 GB SSD
├── OS:       Ubuntu 22.04 LTS (aarch64)
├── Network:  4 Gbps
└── Cost:     $0/month (Oracle Always Free tier)
```

### Container Resource Allocation

| Container | OCPU | RAM | Role |
|---|---|---|---|
| orion-crypto | 2 | 3GB | All ingestion engines |
| orion-api | 2 | 1GB | FastAPI public gateway |
| orion-grafana | 1 | 1GB | War Room dashboard |
| orion-redis | 1 | 1GB | Signal event bus |
| orion-watchdog | 1 | 512MB | Engine health monitor |
| Nginx | 0.5 | 256MB | SSL + reverse proxy |

### Security Configuration
- JWT authentication on all API endpoints (HS256)
- Rate limiting: 120 requests/minute per client
- Redis password-protected
- Nginx SSL termination with Let's Encrypt
- Tailscale VPN for inter-node communication
- Docker network isolation (internal + external bridge)

---

## Observability

### Grafana War Room Panels
- Live price tiles: BTC, ETH, SOL, BNB, XRP, DOGE
- Metals intelligence: Gold, Silver, Copper, MPI gauge
- Composite stress gauges: AI Macro, Crypto Pressure, Cascade Probability
- Signal throughput chart: events/min by domain
- Cross-domain alert feed: plain-English signal interpreter
- COT Smart Money Index: commercial vs speculative divergence
- System telemetry: signal count, active engines, avg trust score

### Structured Logging
```python
# Every engine emits structured JSON logs
{
  "timestamp": "2026-03-15T11:05:34",
  "level": "INFO",
  "engine": "MICRO_ENGINE",
  "message": "Rate: 4836.3 e/min | Errors: 0"
}
```

### Engine Heartbeat System
- Every engine writes heartbeat to `engine_heartbeat` table every 30s
- Global watchdog detects stalled engines within 5 minutes
- Auto-recovery via container restart (Docker socket mounted)
- Alert via Telegram on engine death

---

## Project Structure

```
orion_prime_ingestion/
├── src/aegis_sense/
│   ├── collectors/
│   │   ├── crypto/              # 9 engines — WebSocket + REST
│   │   │   ├── exchanges/       # Binance, Bybit connectors
│   │   │   ├── onchain/         # Whale, mempool, gas monitors
│   │   │   └── analytics/       # Derivatives, liquidation engines
│   │   ├── metals/              # 15 engines — MCX, COMEX, LME
│   │   └── energy/              # EIA, OPEC (building)
│   ├── intelligence/
│   │   ├── engines/             # Domain intelligence engines
│   │   ├── composite/           # Index + regime classifiers
│   │   └── engine_registry.py   # Auto-discovery pattern
│   ├── storage/
│   │   ├── postgres_repo.py     # Async TimescaleDB writer
│   │   └── redis_bus.py         # Signal bus subscriber
│   ├── orchestration/
│   │   └── global_engine_watchdog.py
│   └── api_gateway/             # FastAPI + JWT + WebSocket
├── dashboard/
│   ├── ai_brain/                # Regime classifier
│   ├── compiler/                # Grafana auto-builder
│   └── websocket_bridge/        # Real-time streaming
├── dev_ai/                      # Autonomous AI dev system
├── deployments/
│   ├── docker/                  # Dockerfiles per service
│   ├── kubernetes/              # K8s manifests (ready)
│   ├── terraform/               # IaC (ready)
│   └── nginx/                   # SSL config
├── config/
│   ├── settings.yaml            # Domain + engine config
│   └── domains.yaml             # Asset + interval definitions
└── db/init.sql                  # Schema + hypertables + indexes
```

---

## Quick Start

```bash
# Clone
git clone https://github.com/hhemant86/ORION-CORE.git
cd ORION-CORE/orion_prime_ingestion

# Configure
cp config/.env.example .env
# Add API keys — all free tier sufficient

# Launch
docker-compose up -d

# Verify — should show signal counts within 60 seconds
docker exec orion-postgres psql -U postgres -d ORION \
  -c "SELECT domain, COUNT(*) FROM signal_events GROUP BY domain;"

# Dashboard
open http://localhost:3800   # Grafana War Room
open http://localhost:8100/docs  # FastAPI Swagger
```

---

## Key Engineering Decisions

**Why asyncio over threading?**
Financial data requires thousands of concurrent WebSocket connections with microsecond-level event processing. asyncio's cooperative multitasking eliminates thread overhead and lock contention — 4,800 events/min from a single engine with zero errors.

**Why TimescaleDB over InfluxDB?**
SQL compatibility means zero learning curve for any engineer, full JOIN capability across domains, and JSONB for schema-flexible metadata. TimescaleDB's automatic hypertable partitioning handles time-series at scale without operational complexity.

**Why Redis pub/sub over Kafka?**
At 14M signals/day, Redis handles throughput comfortably with AOF persistence, significantly lower operational overhead, and native async Python client. Kafka becomes the right choice at 100M+ events/day — a future migration path already considered.

**Why local LLM over API-based?**
Zero per-token cost for an autonomous system that runs debug cycles every 5 minutes. Qwen2.5-Coder-7B provides sufficient code quality for fix generation with human approval gates preventing bad patches from reaching production.

---

## Roadmap

| Phase | Status | Deliverable |
|---|---|---|
| Crypto Domain | ✅ Complete | 9 engines, 9.5M+ signals |
| Metals Domain | ✅ Live | 15 engines, 85K+ signals |
| Oracle VM Deployment | 🔄 Active | Always-on production |
| Energy Domain | 📋 Next | EIA + crack spread intelligence |
| Macro Domain | 📋 Planned | Fed, yield curve, FX signals |
| ML Prediction Layer | 📋 Planned | Regime-based price forecasting |
| Kubernetes Migration | 📋 Ready | Manifests already written |

---

## License

Copyright © 2026 ORION PRIME. All rights reserved.
Proprietary and Confidential.

---

<div align="center">

*Built with Python · TimescaleDB · Redis · FastAPI · Docker · Oracle Cloud*

*AEGIS-SENSE v4.0 | Node EB42ECCC | 14.1M+ Signals | LIVE*

</div>
