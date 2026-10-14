from unittest.mock import patch
from src.ingestion.ticketmaster import TicketmasterClient


@patch("requests.get")
def test_fetch_events(mock_get):
    mock_get.return_value.json.return_value = {
        "_embedded": {"events": [{"name": "Test Event"}]}
    }
    client = TicketmasterClient()
    response = client.fetch_events("test", "test_market")
    assert response["_embedded"]["events"][0]["name"] == "Test Event"


def test_standardize_events():
    client = TicketmasterClient()
    raw_data = {"_embedded": {"events": [{"name": "Test Event"}]}}
    df = client.standardize_events(raw_data)
    assert df.shape == (1, 1)
