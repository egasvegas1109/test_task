from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class TensorHomePageLocators:
    BLOCK_POWER_IN_PEOPLE = (
        By.XPATH,
        '//div[@class="tensor_ru-Index__block4-content tensor_ru-Index__card" and .//p[text() = "Сила в людях"]]',
    )

    BUTTON_MORE_DETAILED = (
        By.CSS_SELECTOR,
        'a[href="/about"].tensor_ru-link.tensor_ru-Index__link',
    )


# noinspection SpellCheckingInspection,PyBroadException
class TensorHomePage(BasePage):
    PAGE_URL = "https://tensor.ru"

    def check_block_power_in_people_exist(self):
        """
        Проверяет существует ли блок "Сила в людях".
        """
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(
                    TensorHomePageLocators.BLOCK_POWER_IN_PEOPLE
                ),
                f"Couldn't find element by locator {TensorHomePageLocators.BLOCK_POWER_IN_PEOPLE}",
            )
            return True
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            return False

    def power_in_people_click_button(self):
        """
        Кликает на кнопку "Подробнее" в блоке "Сила в людях".
        """
        button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(TensorHomePageLocators.BUTTON_MORE_DETAILED),
            f"Couldn't find element by locator {TensorHomePageLocators.BUTTON_MORE_DETAILED}",
        )
        # Иногда возникает проблема того, что клик перехвачен, поэтому используем JS
        self.driver.execute_script("arguments[0].click();", button)
