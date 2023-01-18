import pytest
import requests


@pytest.mark.duckduckgo
@pytest.mark.rest_api
def test_request_duckduckgo_api():

    # Arrange
    url = "https://api.duckduckgo.com/?q=python+programming&format=json"

    # Act
    response = requests.get(url, timeout=1000)
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert "Python" in body['AbstractText']