import pytest
from unittest.mock import patch
from src.ingestion.seatgeek import SeatGeekClient

@patch('requests.get')
def test_fetch_events(mock_get):
    mock_get.return_value.json.return_value = {"events": [{"title": "Test Event"}]}
    client = SeatGeekClient()
    response = client.fetch_events("test", "test_venue")
    assert response["events"][0]["title"] == "Test Event"

def test_standardize_events():
    client = SeatGeekClient()
    raw_data = {"events": [{"title": "Test Event"}]}
    df = client.standardize_events(raw_data)
    assert df.shape == (1, 1)
