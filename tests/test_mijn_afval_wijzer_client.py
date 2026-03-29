import pytest
from unittest.mock import patch, MagicMock
from Clients.mijn_afval_wijzer_client import MijnAfvalWijzerClient


def test_init_requires_api_key():
    with pytest.raises(Exception, match="No API key provided"):
        MijnAfvalWijzerClient("")


def test_init_stores_api_key():
    client = MijnAfvalWijzerClient("test-key-123")
    assert client.api_key == "test-key-123"


def test_get_data_returns_none_on_non_200():
    with patch("Clients.mijn_afval_wijzer_client.requests.get") as mock_get:
        mock_get.return_value = MagicMock(status_code=404)
        client = MijnAfvalWijzerClient("test-key")
        result = client.get_data("1234AB", "10")
        assert result is None


def test_get_data_returns_none_on_bad_response():
    with patch("Clients.mijn_afval_wijzer_client.requests.get") as mock_get:
        mock_get.return_value = MagicMock(
            status_code=200,
            json=lambda: {"ophaaldagen": {"response": "ERROR", "data": []}}
        )
        client = MijnAfvalWijzerClient("test-key")
        result = client.get_data("1234AB", "10")
        assert result is None


def test_get_data_returns_data_on_ok_response():
    expected_data = [{"type": "gft", "date": "2024-01-15"}]
    with patch("Clients.mijn_afval_wijzer_client.requests.get") as mock_get:
        mock_get.return_value = MagicMock(
            status_code=200,
            json=lambda: {"ophaaldagen": {"response": "OK", "data": expected_data}}
        )
        client = MijnAfvalWijzerClient("test-key")
        result = client.get_data("1234AB", "10")
        assert result == expected_data
