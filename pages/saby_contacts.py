from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class SabyContactsPageLocators:
    TENSOR_BANNER = (
        By.XPATH,
        '//a[@href="https://tensor.ru/" and @class="sbisru-Contacts__logo-tensor mb-12"]',
    )

    REGION_SELECTOR = (
        By.CSS_SELECTOR,
        "span.sbis_ru-Region-Chooser__text.sbis_ru-link",
    )

    PARTNERS_LIST = (By.CLASS_NAME, "sbisru-Contacts-List__col-1")

    REGIONS_LIST = (By.CSS_SELECTOR, "li.sbis_ru-Region-Panel__item")


# noinspection SpellCheckingInspection
class SabyContactsPage(BasePage):
    PAGE_URL = "https://saby.ru/contacts"

    def click_on_tensor_banner(self):
        """
        Кликает на баннер "Тензор" и переключает драйвер на новую вкладку.
        :return:
        """
        initial_handles = self.driver.window_handles
        banner = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(SabyContactsPageLocators.TENSOR_BANNER),
            f"Couldn't find element by locator {SabyContactsPageLocators.TENSOR_BANNER}",
        )

        # Иногда возникает проблема того, что клик перехвачен, поэтому используем JS
        self.driver.execute_script("arguments[0].click();", banner)

        WebDriverWait(self.driver, 10).until(EC.new_window_is_opened(initial_handles))

        # Переключаемся на новую вкладку, чтобы driver ссылался на неё при работе
        for handle in self.driver.window_handles:
            if handle not in initial_handles:
                self.driver.switch_to.window(handle)
                break

        # Переход на новую страницу осуществляется по click() без driver.get()
        # поэтому используем явное ожидание для полной загрузки
        WebDriverWait(self.driver, 20).until(
            lambda driver: driver.execute_script("return document.readyState")
            == "complete"
        )

    def check_region_selector_exist(self, region_name):
        """
        Проверяет существует ли селектор выбора указанного региона.
        :param region_name: название региона
        :return:
        """
        try:
            selector = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    SabyContactsPageLocators.REGION_SELECTOR
                ),
                f"Couldn't find element by locator {SabyContactsPageLocators.REGION_SELECTOR}",
            )
            if region_name in selector.text:
                return True
            else:
                return False
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            return False

    def get_partners_list(self):
        """
        Получает список партнёров.
        """
        try:
            partners = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(
                    SabyContactsPageLocators.PARTNERS_LIST
                ),
                f"Couldn't find element by locator {SabyContactsPageLocators.PARTNERS_LIST}",
            )
            return [partner.text for partner in partners]
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            return []

    def set_region(self, region_name: str):
        """
        Изменяет регион на указанный.
        :param region_name: название региона
        :return:
        """
        selector = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(SabyContactsPageLocators.REGION_SELECTOR),
            f"Couldn't find element by locator {SabyContactsPageLocators.REGION_SELECTOR}",
        )

        current_region = selector.text

        self.driver.execute_script("arguments[0].click()", selector)

        regions_list = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located(
                SabyContactsPageLocators.REGIONS_LIST
            ),
            f"Couldn't find element by locator {SabyContactsPageLocators.REGIONS_LIST}",
        )

        # Перебираем все li для переключения региона
        for region in regions_list:
            if region_name in region.text:
                region.click()
                break

        # Дожидаемся изменения региона
        WebDriverWait(self.driver, 10).until(
            lambda driver: selector.text != current_region,
            "Region did not update after selection",
        )
