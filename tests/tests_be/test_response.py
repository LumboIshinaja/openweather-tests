from utils.weather_models import WeatherResponseModel
import pytest

@pytest.mark.api
def test_weather_api_response(api_client, get_weather_data):
    """Test that OpenWeather API returns a valid response matching the expected model."""
    city = "Novi Sad"
    api_test_data = get_weather_data(city)
    response = api_client.get(api_test_data["url"])

    # Validate response using Pydantic
    weather_data = WeatherResponseModel(**response.json())
    assert weather_data.name == api_test_data["city"], f"Expected city '{api_test_data['city']}', but got '{weather_data.name}'"
    