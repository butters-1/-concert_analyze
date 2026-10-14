# How to Source Data and Set Up Pipeline

This document describes how to source data from external APIs (like Ticketmaster) and set up a pipeline that
stores the raw data as Parquet files (landing tables) and then loads them into the Data Vault 2.0 raw objects.

## Steps

1. **Source Data from API**
   - Use the TicketmasterClient (or SeatGeekClient) to fetch events.
   - Standardize the data into a common format.

2. **Store as Parquet (Landing Tables)**
   - Write the standardized data to Parquet files in a designated landing directory.
   - Partition the data by date and source for efficiency.

3. **Load into Data Vault 2.0**
    - Use the provided load function to ingest the Parquet files into the Data Vault hubs, links, and satellites.

## Example Code

```python
# Example: Fetch and store Ticketmaster events
from src.ingestion.ticketmaster import TicketmasterClient
from src.ingestion.storage import write_parquet
from src.ingestion.vault import load_to_vault
import polars as pl

client = TicketmasterClient()
raw_data = client.fetch_events(keyword="concert", market_id="US")
events_df = client.standardize_events(raw_data)

# Write to landing area
write_parquet(events_df, provider="ticketmaster", event_date="2024-01-01", ingested_at="2024-01-01T00:00:00")

# For the purpose of this example, we assume we have a separate venues DataFrame.
# In practice, you would extract venue information from the events or from a separate API call.
# Here, we create a dummy venues DataFrame for illustration.
venues_df = pl.DataFrame({
    "venue_id": ["v1", "v2"],
    "venue_name": ["Venue A", "Venue B"],
    "city": ["City X", "City Y"],
    "state": ["State X", "State Y"],
    "country": ["Country X", "Country Y"]
})

# Load into Data Vault
load_to_vault(events_df, venues_df)
```

## Notes

- The `write_parquet` function is defined in `src/ingestion/storage.py`.
- The `load_to_vault` function is defined in `src/ingestion/vault/load.py`.
- Ensure that the Data Vault tables are created by running the SQL script in `src/ingestion/vault/create_tables.sql`.
