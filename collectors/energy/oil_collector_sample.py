# ORION PRIME — Sample Energy Collector
# Oil price collector using FRED API (institutional grade)
# Production version runs on Oracle Cloud VM

import asyncio
import logging
import os
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

import aiohttp

logger = logging.getLogger(__name__)

FRED_BASE = "https://api.stlouisfed.org/fred/series/observations"

FRED_SERIES = {
    "WTI":   "DCOILWTICO",    # West Texas Intermediate
    "BRENT": "DCOILBRENTEU",  # Brent Crude
}


class OilCollector:
    """
    Crude oil price collector using FRED API.
    
    FRED (Federal Reserve Economic Data) is institutional grade:
    - Hosted by St. Louis Federal Reserve
    - No IP restrictions (works from cloud VMs)
    - Mirrors EIA data with same-day publication
    - No rate limits on free tier
    
    Emits SignalEvent to TimescaleDB via PostgresRepo.
    Poll interval: 3600s (daily data cadence)
    """

    COLLECTOR_NAME = "oil_collector"
    DOMAIN = "ENERGY"

    def __init__(self):
        self._running = False
        self._last_prices: Dict[str, float] = {}

    async def start(self):
        self._running = True
        logger.info("OilCollector starting | source=FRED | WTI+BRENT")
        async with aiohttp.ClientSession() as session:
            self._session = session
            await self._collection_loop()

    async def _collection_loop(self):
        while self._running:
            try:
                records = await self._fetch_all()
                if records:
                    await self._emit(records)
                    logger.info("OilCollector cycle OK | %s",
                                {k: round(v,2) for k,v in self._last_prices.items()})
            except Exception as exc:
                logger.error("OilCollector error: %s", exc)
            await asyncio.sleep(3600)

    async def _fetch_all(self) -> List[Dict[str, Any]]:
        api_key = os.environ.get("FRED_API_KEY", "")
        results = []
        fetched_at = datetime.now(timezone.utc)

        for asset, series_id in FRED_SERIES.items():
            price = await self._fetch_fred(series_id, asset, api_key)
            if price and 5.0 <= price <= 500.0:
                results.append({
                    "asset": asset,
                    "price": price,
                    "unit": "USD/barrel",
                    "fetched_at": fetched_at,
                })
                self._last_prices[asset] = price

        # Compute WTI-Brent spread
        if "WTI" in self._last_prices and "BRENT" in self._last_prices:
            spread = round(self._last_prices["WTI"] - self._last_prices["BRENT"], 4)
            results.append({
                "asset": "WTI_BRENT_SPREAD",
                "price": spread,
                "unit": "USD/barrel",
                "fetched_at": fetched_at,
            })

        return results

    async def _fetch_fred(self, series_id: str, asset: str, api_key: str) -> Optional[float]:
        params = {
            "series_id": series_id,
            "api_key": api_key,
            "sort_order": "desc",
            "limit": "10",
            "file_type": "json",
        }
        async with self._session.get(FRED_BASE, params=params) as resp:
            if resp.status != 200:
                return None
            data = await resp.json(content_type=None)
            for obs in data.get("observations", []):
                val = obs.get("value", ".")
                if val and val != ".":
                    logger.info("FRED | %s = %.4f USD/bbl | date=%s",
                                asset, float(val), obs.get("date"))
                    return float(val)
        return None

    async def _emit(self, records: List[Dict[str, Any]]):
        # In production: emits to TimescaleDB via PostgresRepo
        # Schema: signal_events(domain, asset, source, data_type, value, unit, trust_score)
        for r in records:
            logger.debug("EMIT | %s = %.4f %s", r["asset"], r["price"], r["unit"])
