import os
import pytest
from unittest.mock import patch, MagicMock
from Clients.slack_client import SlackClient


def test_init_token_from_env():
    with patch.dict(os.environ, {"SLACK_TOKEN": "xoxb-test-token"}):
        client = SlackClient()
        assert client.token == "xoxb-test-token"


def test_init_no_token():
    os.environ.pop("SLACK_TOKEN", None)
    client = SlackClient()
    assert client.token == ""


def test_send_calls_requests_post():
    with patch("Clients.slack_client.requests.post") as mock_post:
        mock_post.return_value = MagicMock()
        mock_post.return_value.json.return_value = {}
        client = SlackClient()
        client.send("hello", "#general")
        mock_post.assert_called_once()


def test_send_with_blocks():
    with patch("Clients.slack_client.requests.post") as mock_post:
        mock_post.return_value = MagicMock()
        mock_post.return_value.json.return_value = {}
        client = SlackClient()
        blocks = [{"type": "section", "text": {"type": "mrkdwn", "text": "test"}}]
        client.send("hello", "#general", blocks=blocks)
        mock_post.assert_called_once()
