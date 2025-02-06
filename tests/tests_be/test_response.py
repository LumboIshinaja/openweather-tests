from utils.config import API_KEY, BASE_URL
from utils.weather_models import WeatherResponse

def test_weather_api_response(api_client):
    """Test that OpenWeather API returns a valid response matching the expected model."""
    city = "Novi Sad"
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}"
    response = api_client.get(url)

    # Validate response using Pydantic
    weather_data = WeatherResponse(**response.json())
    assert weather_data.name == city, f"Expected city '{city}', but got '{weather_data.name}'"
