import pytest

@pytest.mark.ui
def test_search_city_weather(weather_ui):
    """Test searching for Novi Sad's weather on OpenWeather's UI."""
    
    # Search for Novi Sad
    city_name = "Novi Sad"
    weather_ui.search_city(city_name)

    # Validate that the result contains the correct city name
    city_heading = weather_ui.page.get_by_role("heading", name=city_name).text_content()
    assert city_name in city_heading, f"Expected '{city_name}' in heading, but got '{city_heading}'"
