import pytest

@pytest.mark.api
def test_weather_api_status(api_client, get_weather_data):
    """Test that the OpenWeather API is reachable and returns a 200 status."""
    response = api_client.get(get_weather_data["url"])
    
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
