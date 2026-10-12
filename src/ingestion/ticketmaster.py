import os
import requests
import polars as pl
from datetime import datetime, timezone

class TicketmasterClient:
    def __init__(self):
        self.api_key = os.getenv("TICKETMASTER_API_KEY")
        self.base_url = "https://app.ticketmaster.com/discovery/v2/events.json"

    def fetch_events(self, keyword: str, market_id: str) -> dict:
        params = {
            "apikey": self.api_key,
            "keyword": keyword,
            "marketId": market_id,
            "locale": "en-us",
            "size": 200
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        return response.json()

    def standardize_events(self, raw_data: dict) -> pl.DataFrame:
        events = []
        for event in raw_data.get("_embedded", {}).get("events", []):
            event_id = event.get("id")
            event_name = event.get("name")
            event_datetime = event.get("dates", {}).get("start", {}).get("dateTime")
            ingested_at = datetime.now(timezone.utc)
            days_until_event = (datetime.fromisoformat(event_datetime) - ingested_at).days if event_datetime else None
            price_ranges = event.get("priceRanges", [])
            min_price = min(pr["min"] for pr in price_ranges) if price_ranges else None
            max_price = max(pr["max"] for pr in price_ranges) if price_ranges else None
            listing_count = event.get("pleaseNote", {}).get("listingCount")

            snapshot_id = f"ticketmaster_{event_id}_{int(ingested_at.timestamp())}"

            events.append({
                "snapshot_id": snapshot_id,
                "provider": "ticketmaster",
                "event_id": event_id,
                "event_name": event_name,
                "event_datetime": datetime.fromisoformat(event_datetime) if event_datetime else None,
                "ingested_at": ingested_at,
                "days_until_event": days_until_event,
                "min_price": min_price,
                "median_price": None,
                "max_price": max_price,
                "listing_count": listing_count,
            })

        return pl.DataFrame(events).with_columns(
            pl.col("event_datetime").cast(pl.Datetime("UTC")),
            pl.col("ingested_at").cast(pl.Datetime("UTC")),
        )
