import os
import pytest
from unittest.mock import patch, MagicMock
from Clients.mongodb_client import MongoDBClient


@patch("Clients.mongodb_client.MongoClient")
def test_init_creates_mongo_client(mock_mongo):
    mock_client = MagicMock()
    mock_mongo.return_value = mock_client
    client = MongoDBClient()
    mock_mongo.assert_called_once()


@patch("Clients.mongodb_client.MongoClient")
def test_get_client(mock_mongo):
    mock_instance = MagicMock()
    mock_mongo.return_value = mock_instance
    client = MongoDBClient()
    assert client.get_client() == mock_instance


@patch("Clients.mongodb_client.MongoClient")
def test_get_host_default(mock_mongo):
    client = MongoDBClient()
    assert client.get_host() == "localhost"


@patch("Clients.mongodb_client.MongoClient")
def test_get_port_default(mock_mongo):
    client = MongoDBClient()
    assert client.get_port() == 27017


@patch("Clients.mongodb_client.MongoClient")
def test_get_host_from_env(mock_mongo):
    with patch.dict(os.environ, {"MONGO_DB_HOST": "mongo.example.com"}):
        client = MongoDBClient()
        assert client.get_host() == "mongo.example.com"


@patch("Clients.mongodb_client.MongoClient")
def test_get_db_name_from_env(mock_mongo):
    with patch.dict(os.environ, {"MONGO_DB_DB": "mydb"}):
        client = MongoDBClient()
        assert client.get_db_name() == "mydb"
