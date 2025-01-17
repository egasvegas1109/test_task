import re
import os
import time
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


# noinspection SpellCheckingInspection,PyTypeChecker
class SabyDownloadPage(BasePage):
    PAGE_URL = "https://saby.ru/download"

    def set_operating_system(self, os_name: str):
        """
        Выбирает указанную операционную систему.
        :param os_name: название ОС
        """
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

    def set_product_download(self, product_name: str):
        """
        Выбирает указанный продукт.
        :param product_name: название продукта
        """
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
        """
        Скачивает веб-установщик для Saby Plugin Windows, ожидает завершения загрузки,
        и проверяет, что размер скачанного файла соответствует ожидаемому.
        """
        url_download = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(
                SabyDownloadPageLocators.DOWNLOAD_WINDOWS_WEB_VERSION_URL
            ),
            f"Couldn't find element by locator {SabyDownloadPageLocators.DOWNLOAD_WINDOWS_WEB_VERSION_URL}",
        )
        url_download.click()

        # Получаем ссылку на скачивание
        href_value = url_download.get_attribute("href")

        # Получаем ожидаемый размер файла по данным с сайта
        expected_file_size = float(re.search("\d+\.\d+", url_download.text).group())

        # Получаем название скачиваемого файла из ссылки
        file_name = re.search("[a-zA-Z-]*\.(exe|msi)", href_value).group()

        # Получаем текущую рабочую директорию и добавляем путь до файла
        download_dir = os.getcwd()
        file_path = os.path.join(download_dir, file_name)

        start_time = time.time()
        timeout = 30

        while True:
            if os.path.exists(file_path):
                actual_file_size = round(os.path.getsize(file_path) / 1024 / 1024, 2)
                if expected_file_size == actual_file_size:
                    return True

            # Для исключения возможности бесконечного цикла
            if time.time() - start_time > timeout:
                return False
