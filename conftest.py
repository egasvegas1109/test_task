import pytest
import os
from selenium import webdriver


@pytest.fixture(scope="session")
def create_web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-features=InsecureDownloadWarnings")
    download_dir = os.getcwd()

    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    }

    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
