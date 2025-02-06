import pytest
import requests
from playwright.sync_api import sync_playwright

# ✅ Fixture for API tests (requests session)
@pytest.fixture(scope="session")
def api_client():
    """Creates a session for API requests."""
    session = requests.Session()
    yield session
    session.close()

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
