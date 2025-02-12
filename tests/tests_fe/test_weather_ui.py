import pytest

@pytest.fixture
def search_city_fixture(main_page):
    """Fixture to search for a city and return the page."""
    city_name = "Novi Sad"
    main_page.search_city(city_name)
    return main_page.page 

@pytest.mark.ui
def test_city_name_displayed(search_city_fixture):
    """Test that the searched city name is correctly displayed."""
    city_name = "Novi Sad"
    city_heading = search_city_fixture.get_by_role("heading", name=city_name).text_content()
    assert city_name in city_heading, f"Expected '{city_name}' in heading, but got '{city_heading}'"

@pytest.mark.ui
def test_temperature_displayed(search_city_fixture):
    """Test that the temperature is displayed on the UI."""
    temperature = search_city_fixture.locator(".current-temp span").text_content()
    assert temperature, "Temperature is not displayed on UI"

@pytest.mark.ui
def test_weather_description_displayed(search_city_fixture):
    """Test that the weather description (e.g., 'Cloudy') is displayed."""
    weather_description = search_city_fixture.locator(".current-container .bold").text_content()
    assert weather_description, "Weather description is missing"

@pytest.mark.ui
def test_humidity_displayed(search_city_fixture):
    """Test that humidity data is displayed."""
    humidity = search_city_fixture.locator(".weather-items.text-container.orange-side.standard-padding").text_content()
    assert humidity, "Humidity data is missing"

@pytest.mark.ui
def test_wind_speed_displayed(search_city_fixture):
    """Test that wind speed is displayed on the UI."""
    wind_speed = search_city_fixture.locator(".weather-items.text-container.orange-side.standard-padding").text_content()
    assert wind_speed, "Wind speed data is missing"
