from playwright.sync_api import Page
from pages.weather_page import WeatherPage

def test_search_city_weather(page):
    """Test searching for Novi Sad's weather on OpenWeather's UI."""
    weather_page = WeatherPage(page)
    weather_page.open()
    
    # Search for Novi Sad
    city_name = "Novi Sad"
    weather_page.search_city(city_name)

    # Validate that the result contains the correct city name
    city_heading = page.get_by_role("heading", name=city_name).text_content()
    assert city_name in city_heading, f"Expected '{city_name}' in heading, but got '{city_heading}'"
