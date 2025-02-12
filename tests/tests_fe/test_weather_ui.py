import pytest

@pytest.mark.ui
def test_city_name_displayed(main_page):
    """Test that the searched city name is correctly displayed."""
    city_name = "Novi Sad"
    main_page.search_city(city_name)

    city_heading = main_page.page.get_by_role("heading", name=city_name).text_content()
    assert city_name in city_heading, f"Expected '{city_name}' in heading, but got '{city_heading}'"

@pytest.mark.ui
def test_temperature_displayed(main_page):
    """Test that the temperature is displayed on the UI."""
    city_name = "Novi Sad"
    main_page.search_city(city_name)

    temperature = main_page.page.locator(".current-temp span").text_content()
    assert temperature, "Temperature is not displayed on UI"

@pytest.mark.ui
def test_weather_description_displayed(main_page):
    """Test that the weather description (e.g., 'Cloudy') is displayed."""
    city_name = "Novi Sad"
    main_page.search_city(city_name)

    weather_description = main_page.page.locator(".current-container .bold").text_content()
    assert weather_description, "Weather description is missing"

@pytest.mark.ui
def test_humidity_displayed(main_page):
    """Test that humidity data is displayed."""
    city_name = "Novi Sad"
    main_page.search_city(city_name)

    humidity = main_page.page.locator(".weather-items.text-container.orange-side.standard-padding").text_content()
    assert humidity, "Humidity data is missing"

@pytest.mark.ui
def test_wind_speed_displayed(main_page):
    """Test that wind speed is displayed on the UI."""
    city_name = "Novi Sad"
    main_page.search_city(city_name)

    wind_speed = main_page.page.locator(".weather-items.text-container.orange-side.standard-padding").text_content()
    assert wind_speed, "Wind speed data is missing"
