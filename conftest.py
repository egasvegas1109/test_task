import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def create_web_driver():
    driver = webdriver.Safari()
    driver.maximize_window()
    yield driver
    driver.quit()
