from utils.config import API_KEY, BASE_URL

def test_weather_api_status(api_client):
    """Test that the OpenWeather API is reachable and returns a 200 status."""
    city = "Novi Sad"
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}"
    response = api_client.get(url)
    
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
