from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class SabyContactsPageLocators:
    TENSOR_BANNER = (
        By.XPATH,
        '//a[@href="https://tensor.ru/"][@class="sbisru-Contacts__logo-tensor mb-12"]',
    )

    REGION_SELECTOR = (
        By.CSS_SELECTOR,
        'span.sbis_ru-Region-Chooser__text.sbis_ru-link'
    )

    PARTNERS_LIST = (
        By.XPATH,
        '//div[@name="itemsContainer" and @data-qa="items-container"]//div[@data-qa="item"]'
    )

    REGIONS_LIST = (
        By.CSS_SELECTOR,
        'li.sbis_ru-Region-Panel__item'
    )

    REGIONS_TAB_CLOSE_BUTTON = (
        By.CLASS_NAME,
        'sbis_ru-Region-Panel__header-close'
    )


# noinspection SpellCheckingInspection
class SabyContactsPage(BasePage):
    PAGE_URL = "https://sbis.ru/contacts/"

    def click_on_tensor_banner(self):
        initial_handles = self.driver.window_handles
        banner = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(SabyContactsPageLocators.TENSOR_BANNER),
            f"Couldn't find element by locator {SabyContactsPageLocators.TENSOR_BANNER}",
        )

        #Иногда возникает проблема того, что клик перехвачен, поэтому используем JS
        self.driver.execute_script("arguments[0].click();", banner)

        WebDriverWait(self.driver, 10).until(
            EC.new_window_is_opened(initial_handles)
        )

        #Переключаемся на новую вкладку, чтобы driver ссылался на неё при работе
        for handle in self.driver.window_handles:
            if handle not in initial_handles:
                self.driver.switch_to.window(handle)
                break

        #Переход на новую страницу осуществляется по click() без driver.get()
        #поэтому используем явное ожидание для полной загрузки
        WebDriverWait(self.driver, 20).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete'
        )

    def check_region_selector_exist(self, region_name):
        try:
            selector = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(SabyContactsPageLocators.REGION_SELECTOR),
                f"Couldn't find element by locator {SabyContactsPageLocators.REGION_SELECTOR}",
            )
            if region_name in selector.text:
                return True
            else:
                return False
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            return  False

    def check_partners_list_exist(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(SabyContactsPageLocators.PARTNERS_LIST),
                f"Couldn't find element by locator {SabyContactsPageLocators.PARTNERS_LIST}",
            )
            return True
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            return False

    def set_region(self, region_name):
        selector = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(SabyContactsPageLocators.REGION_SELECTOR),
            f"Couldn't find element by locator {SabyContactsPageLocators.REGION_SELECTOR}",
        )

        selector.click()

        #self.driver.execute_script("arguments[0].click();", selector)

        regions_list = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located(SabyContactsPageLocators.REGIONS_LIST),
            f"Couldn't find element by locator {SabyContactsPageLocators.REGIONS_LIST}",
        )

        for region in regions_list:
            if region_name in region.text:
                region.click()
                break

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(SabyContactsPageLocators.REGIONS_TAB_CLOSE_BUTTON),
            f"Couldn't find element by locator {SabyContactsPageLocators.REGIONS_TAB_CLOSE_BUTTON}",
        ).click()






