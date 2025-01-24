import pytest
from requests.cookies import MockResponse

from b2b_sdk.client import YellowCard


def test_get_resource(mocker):
    mock_response = {"id": "123", "name": "Test Resource", "status": "active"}
    mocker.patch("requests.request", return_value=MockResponse(mock_response, 200))

    client = YellowCard(base_url="https://api.example.com", api_key="test_key")
    resource = client.get_resource("123")
    assert resource["name"] == "Test Resource"
