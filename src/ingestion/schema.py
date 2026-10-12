import polars as pl

EVENT_SNAPSHOT_SCHEMA = {
    "snapshot_id": pl.Utf8,
    "provider": pl.Utf8,
    "event_id": pl.Utf8,
    "event_name": pl.Utf8,
    "event_datetime": pl.Datetime("UTC"),
    "ingested_at": pl.Datetime("UTC"),
    "days_until_event": pl.Float64,
    "min_price": pl.Float64,
    "median_price": pl.Float64.nullable(),
    "max_price": pl.Float64,
    "listing_count": pl.Int64.nullable(),
}
