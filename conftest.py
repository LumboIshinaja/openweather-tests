import pytest
import requests
from playwright.sync_api import sync_playwright
from utils.config import API_KEY, BASE_URL
from pages.main_page_search import MainPageSearch  

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
    """Provides a function to generate API URLs for different cities."""
    def _get_data(city):
        url = f"{BASE_URL}weather?q={city}&appid={API_KEY}"
        return {"city": city, "url": url}
    return _get_data

# ✅ Fixture for Playwright Browser (UI tests)
@pytest.fixture(scope="session")
def browser():
    """Launches Playwright browser for UI tests."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Change to False if you want headed mode
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
def main_page(page):
    """Provides a MainPageSearch instance for UI tests."""
    main_page = MainPageSearch(page)
    main_page.open()
    return main_page