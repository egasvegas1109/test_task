import re
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SabyDownloadPageLocators:
    OPERATION_SYSTEM_BUTTONS = (
        By.XPATH,
        '//div[@class="controls-TabControl-tabButtons"]//span[text()="Windows" or text()="Linux" or text()="MacOS"]',
    )

    PRODUCT_BUTTONS = (
        By.CSS_SELECTOR,
        "div.controls-TabButtons.sbis_ru-VerticalTabs__tabs div.controls-TabButton__caption",
    )

    DOWNLOAD_WINDOWS_WEB_VERSION_URL = (
        By.XPATH,
        "//div[contains(@class, 'sbis_ru-DownloadNew-block')]//h3[contains(text(), 'Веб-установщик')]/../..//a",
    )


# noinspection SpellCheckingInspection
class SabyDownloadPage(BasePage):
    PAGE_URL = "https://saby.ru/download"

    def set_operating_system(self, os_name):
        header_buttons = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(
                SabyDownloadPageLocators.OPERATION_SYSTEM_BUTTONS
            ),
            f"Couldn't find element by locator {SabyDownloadPageLocators.OPERATION_SYSTEM_BUTTONS}",
        )

        for button in header_buttons:
            if os_name in button.text:
                self.driver.execute_script("arguments[0].click();", button)
                return

    def set_product_download(self, product_name):
        product_buttons = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(
                SabyDownloadPageLocators.PRODUCT_BUTTONS
            ),
            f"Couldn't find element by locator {SabyDownloadPageLocators.PRODUCT_BUTTONS}",
        )

        for button in product_buttons:
            if product_name in button.text:
                self.driver.execute_script("arguments[0].click();", button)
                return

    def download_product_web_version(self):
        url_download = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(
                SabyDownloadPageLocators.DOWNLOAD_WINDOWS_WEB_VERSION_URL
            ),
            f"Couldn't find element by locator {SabyDownloadPageLocators.DOWNLOAD_WINDOWS_WEB_VERSION_URL}",
        )
        url_download.click()

        href_value = url_download.get_attribute("href")

        file_size = re.search("\d+\.\d+", url_download.text).group()
        file_name = re.search("[a-zA-Z-]*\.(exe|msi)", href_value).group()

        print(file_name, file_size)
