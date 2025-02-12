import pytest

# ✅ Shared fixture to fetch API response
@pytest.fixture
def fetch_weather_response(api_client, get_weather_data):
    """Fetches the weather API response for a given city."""
    def _fetch(city):
        api_test_data = get_weather_data(city)
        return api_client.get(api_test_data["url"])
    return _fetch

@pytest.mark.api
def test_weather_api_status(fetch_weather_response):
    """Test that the OpenWeather API is reachable and returns a 200 status."""
    response = fetch_weather_response("Novi Sad")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

@pytest.mark.api
def test_api_response_time(fetch_weather_response):
    """Test that the API response time is within acceptable limits (under 1 second)."""
    response = fetch_weather_response("Novi Sad")
    assert response.elapsed.total_seconds() < 1, (
        f"API response took too long: {response.elapsed.total_seconds()}s"
    )

@pytest.mark.api
@pytest.mark.parametrize("invalid_city", ["NoviSad", "."]) 
def test_invalid_city(fetch_weather_response, invalid_city):
    """Test API response for invalid city names, expecting a 404 error."""
    response = fetch_weather_response(invalid_city)
    assert response.status_code == 404, f"Expected 404 for invalid city, but got {response.status_code}"
