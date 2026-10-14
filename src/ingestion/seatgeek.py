import os
import requests
import polars as pl
from datetime import datetime, timezone


class SeatGeekClient:
    def __init__(self):
        self.client_id = os.getenv("SEATGEEK_CLIENT_ID")
        self.client_secret = os.getenv("SEATGEEK_SECRET")
        self.base_url = "https://api.seatgeek.com/2/events"

    def fetch_events(self, q, venue_id):
        params = {
            "q": q,
            "venue_id": venue_id,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        return response.json()

    def standardize_events(self, raw_data):
        events = []
        for event in raw_data.get("events", []):
            event_id = event.get("id")
            event_name = event.get("title")
            event_datetime = event.get("datetime_local")
            ingested_at = datetime.now(timezone.utc)
            days_until_event = None
            if event_datetime:
                try:
                    # Handle ISO format with or without Z
                    if event_datetime.endswith("Z"):
                        event_datetime = event_datetime[:-1] + "+00:00"
                    event_dt = datetime.fromisoformat(event_datetime)
                    days_until_event = (event_dt - ingested_at).days
                except Exception:
                    pass

            # Extract price information - SeatGeek API structure may vary
            # For now, we'll set prices to None as we don't have the exact structure
            min_price = None
            median_price = None
            max_price = None
            listing_count = None  # SeatGeek might not have this field

            snapshot_id = f"seatgeek_{event_id}_{int(ingested_at.timestamp())}"

            events.append(
                {
                    "snapshot_id": snapshot_id,
                    "provider": "seatgeek",
                    "event_id": event_id,
                    "event_name": event_name,
                    "event_datetime": event_datetime,
                    "ingested_at": ingested_at,
                    "days_until_event": days_until_event,
                    "min_price": min_price,
                    "median_price": median_price,
                    "max_price": max_price,
                    "listing_count": listing_count,
                }
            )

        df = pl.DataFrame(events)
        if not df.is_empty():
            df = df.with_columns(
                pl.col("event_datetime").cast(pl.Datetime("UTC")),
                pl.col("ingested_at").cast(pl.Datetime("UTC")),
            )
        return df
