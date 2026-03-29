import os
import pytest
from unittest.mock import patch, MagicMock
from Clients.redis_client import RedisClient


@patch("Clients.redis_client.redis.StrictRedis")
def test_init_creates_redis_client(mock_redis):
    mock_instance = MagicMock()
    mock_redis.return_value = mock_instance
    client = RedisClient()
    mock_redis.assert_called_once()
    assert client.get_client() == mock_instance


@patch("Clients.redis_client.redis.StrictRedis")
def test_get_host_default(mock_redis):
    client = RedisClient()
    assert client.get_host() == "localhost"


@patch("Clients.redis_client.redis.StrictRedis")
def test_get_host_from_env(mock_redis):
    with patch.dict(os.environ, {"REDIS_DB_ADDRESS": "redis.example.com"}):
        client = RedisClient()
        assert client.get_host() == "redis.example.com"


@patch("Clients.redis_client.redis.StrictRedis")
def test_get_port_default(mock_redis):
    client = RedisClient()
    assert client.get_port() == 6379


@patch("Clients.redis_client.redis.StrictRedis")
def test_get_port_from_env(mock_redis):
    with patch.dict(os.environ, {"REDIS_DB_PORT": "6380"}):
        client = RedisClient()
        assert client.get_port() == 6380
