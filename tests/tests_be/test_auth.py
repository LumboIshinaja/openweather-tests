import pytest
from utils.config import API_KEY

@pytest.mark.api
def test_missing_api_key(api_client, get_weather_data):
    """Test API response when no API key is provided, expecting a 401 error."""
    api_test_data = get_weather_data("Novi Sad")
    url = api_test_data["url"].split("&appid=")[0]  # Remove API key

    response = api_client.get(url)
    assert response.status_code == 401, f"Expected 401 for missing API key, but got {response.status_code}"

@pytest.mark.api
def test_invalid_api_key(api_client, get_weather_data):
    """Test API response with an invalid API key, expecting a 401 error."""
    api_test_data = get_weather_data("Novi Sad")
    
    # Replace the API key in the URL
    url = api_test_data["url"].replace(f"appid={API_KEY}", "appid=INVALID_API_KEY")

    response = api_client.get(url)
    assert response.status_code == 401, f"Expected 401 for invalid API key, but got {response.status_code}"

