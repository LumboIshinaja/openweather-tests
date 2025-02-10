import pytest
import requests
from playwright.sync_api import sync_playwright
from utils.config import API_KEY, BASE_URL
from pages.weather_page import WeatherPage

# ✅ Fixture for API tests (requests session)
@pytest.fixture(scope="session")
def api_client():
    """Creates a session for API requests."""
    session = requests.Session()
    yield session
    session.close()

# ✅ Fixture for API tests (test setup)
@pytest.fixture(scope="module")
def get_weather_data():
    """Provides shared test data for API tests."""
    city = "Novi Sad"
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}"
    return {"city": city, "url": url}

# ✅ Fixture for Playwright Browser (UI tests)
@pytest.fixture(scope="session")
def browser():
    """Launches Playwright browser for UI tests."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Change to True if you want headless mode
        yield browser
        browser.close()

# ✅ Fixture for Playwright Page (UI tests)
@pytest.fixture(scope="function")
def page(browser):
    """Creates a new browser page for each test."""
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()

# ✅ Fixture for UI tests (test setup)
@pytest.fixture(scope="function")
def weather_ui(page):
    """Provides a WeatherPage instance for UI tests."""
    weather_page = WeatherPage(page)
    weather_page.open()
    return weather_page