import pytest
from utils.config import API_KEY

# Shared fixture to generate API URLs with different key scenarios
@pytest.fixture
def generate_api_url(get_weather_data):
    """Generates an API request URL with valid, missing, or invalid API keys."""
    def _generate(city, api_key=None):
        api_test_data = get_weather_data(city)
        url = api_test_data["url"]

        if api_key is None:
            # Remove API key (simulate missing key)
            url = url.split("&appid=")[0]
        else:
            # Replace API key (simulate invalid key)
            url = url.replace(f"appid={API_KEY}", f"appid={api_key}")

        return url

    return _generate

@pytest.mark.api
def test_missing_api_key(api_client, generate_api_url):
    """Test API response when no API key is provided, expecting a 401 error."""
    url = generate_api_url("Novi Sad", api_key=None)
    response = api_client.get(url)
    assert response.status_code == 401, f"Expected 401 for missing API key, but got {response.status_code}"

@pytest.mark.api
def test_invalid_api_key(api_client, generate_api_url):
    """Test API response with an invalid API key, expecting a 401 error."""
    url = generate_api_url("Novi Sad", api_key="INVALID_API_KEY")
    response = api_client.get(url)
    assert response.status_code == 401, f"Expected 401 for invalid API key, but got {response.status_code}"
