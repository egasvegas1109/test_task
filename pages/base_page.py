from selenium.webdriver.safari.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def go_to_site(self):
        return self.driver.get(self.PAGE_URL)

    def get_current_url(self):
        return self.driver.current_url
