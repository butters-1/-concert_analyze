import os
import polars as pl


def write_parquet(df: pl.DataFrame, provider: str, event_date: str, ingested_at: str):
    base_path = "data/raw"
    provider_path = os.path.join(base_path, provider)
    event_date_path = os.path.join(provider_path, event_date)
    ingested_at_path = os.path.join(event_date_path, ingested_at)
    os.makedirs(ingested_at_path, exist_ok=True)
    parquet_file_path = os.path.join(ingested_at_path, f"data_{ingested_at}.parquet")
    df.write_parquet(parquet_file_path)
