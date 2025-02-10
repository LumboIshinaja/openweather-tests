from playwright.sync_api import Page

class MainPageSearch:
    def __init__(self, page: Page):
        self.page = page
        self.search_box = "input[placeholder='Search city']"
        self.search_button = "button[type='submit']"
        self.temp_display = ".current-temp"

    def open(self):
        """OpenWeather main page."""
        self.page.goto("https://openweathermap.org")

    def search_city(self, city_name: str):
        """Search for a city's weather."""
        self.page.fill(self.search_box, city_name)
        self.page.click(self.search_button)
        self.page.wait_for_selector(self.temp_display)
        self.page.get_by_text(city_name).click()

    def get_temperature(self):
        """Get the displayed temperature."""
        return self.page.text_content(self.temp_display)
