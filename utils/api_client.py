import requests
from utils.config import API_KEY, BASE_URL

class APIClient:
    @staticmethod
    def get_weather(city):
        """Fetch weather data for a city using OpenWeather API."""
        url = f"{BASE_URL}weather?q={city}&appid={API_KEY}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None
