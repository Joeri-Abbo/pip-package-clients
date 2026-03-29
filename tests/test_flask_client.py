import os
import pytest
from unittest.mock import patch
from Clients.flask_client import FlaskClient


def test_get_port_default():
    client = FlaskClient()
    assert client.get_port() == 5033


def test_get_port_from_env():
    with patch.dict(os.environ, {"PORT": "8080"}):
        client = FlaskClient()
        assert client.get_port() == 8080


def test_get_host_default():
    client = FlaskClient()
    assert client.get_host() == "0.0.0.0"


def test_get_host_from_env():
    with patch.dict(os.environ, {"HOST": "127.0.0.1"}):
        client = FlaskClient()
        assert client.get_host() == "127.0.0.1"


def test_get_debug_default():
    with patch.dict(os.environ, {}, clear=False):
        os.environ.pop("DEBUG", None)
        client = FlaskClient()
        assert client.get_debug() is False


def test_get_debug_true():
    with patch.dict(os.environ, {"DEBUG": "True"}):
        client = FlaskClient()
        client.debug = None  # reset cached value
        assert client.get_debug() is True


def test_get_base_url():
    with patch.dict(os.environ, {"HOST": "localhost", "PORT": "5000"}):
        client = FlaskClient()
        assert client.get_base_url() == "http://localhost:5000"


def test_get_client_returns_flask_app():
    from flask import Flask
    client = FlaskClient()
    app = client.get_client()
    assert isinstance(app, Flask)
