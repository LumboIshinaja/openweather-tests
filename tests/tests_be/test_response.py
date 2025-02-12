from utils.weather_models import WeatherResponseModel
import pytest

# Fixture to fetch API response once per test
@pytest.fixture
def fetch_weather_data(api_client, get_weather_data):
    """Fetches the API response for a given city."""
    def _fetch(city):
        api_test_data = get_weather_data(city)
        response = api_client.get(api_test_data["url"])
        return response
    return _fetch

# Fixture to extract key weather fields
@pytest.fixture
def extract_weather_fields(fetch_weather_data):
    """Extracts weather data fields from the API response."""
    def _extract(city):
        response = fetch_weather_data(city)
        data = response.json()
        return {
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "response_json": data,
        }
    return _extract

@pytest.mark.api
def test_weather_api_response(fetch_weather_data, get_weather_data):
    """Test that OpenWeather API returns a valid response matching the expected model."""
    city = "Novi Sad"
    response = fetch_weather_data(city)

    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    assert response.headers["Content-Type"] == "application/json; charset=utf-8", "Response is not JSON"

    # Validate response using Pydantic
    weather_data = WeatherResponseModel(**response.json())
    assert weather_data.name == get_weather_data(city)["city"], f"Expected city '{city}', but got '{weather_data.name}'"

@pytest.mark.api
@pytest.mark.parametrize("required_field", ["main", "wind", "weather"])
def test_weather_response_contains_required_fields(fetch_weather_data, required_field):
    """Test that the API response contains required weather data fields."""
    city = "Novi Sad"
    response = fetch_weather_data(city)
    data = response.json()

    assert required_field in data, f"Response missing '{required_field}' section"

@pytest.mark.api
def test_weather_response_valid_temperature(extract_weather_fields):
    """Test that the temperature value is within a realistic range (173K to 333K)."""
    city = "Novi Sad"
    temp = extract_weather_fields(city)["temp"]

    # Kelvin temperature range
    assert 173 <= temp <= 333, f"Temperature {temp}K is out of expected range (173K to 333K)"

@pytest.mark.api
def test_weather_response_valid_humidity(extract_weather_fields):
    """Test that humidity value is between 0% and 100%."""
    city = "Novi Sad"
    humidity = extract_weather_fields(city)["humidity"]

    assert 0 <= humidity <= 100, f"Humidity {humidity}% is out of expected range (0-100%)"

@pytest.mark.api
def test_weather_response_valid_wind_speed(extract_weather_fields):
    """Test that wind speed is a non-negative value."""
    city = "Novi Sad"
    wind_speed = extract_weather_fields(city)["wind_speed"]

    assert wind_speed >= 0, f"Wind speed {wind_speed} m/s cannot be negative"
