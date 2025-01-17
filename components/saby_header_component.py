from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SabyHeaderLocators:
    BUTTONS_HEADER = (
        By.CSS_SELECTOR,
        "li.sbisru-Header__menu-item.mh-8.s-Grid--hide-sm",
    )

    BUTTON_CONTACTS = (
        By.CSS_SELECTOR,
        "a[href='/contacts'].sbisru-link.sbis_ru-link",
    )


# noinspection SpellCheckingInspection
class SabyHeader(BasePage):

    def click_on_button_header(self, header_button: str):
        """
        Кликает на указанную кнопку в шапке сайта.
        :param header_button: название кнопки
        """
        header_buttons = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(SabyHeaderLocators.BUTTONS_HEADER),
            f"Couldn't find element by locator {SabyHeaderLocators.BUTTONS_HEADER}",
        )

        for button in header_buttons:
            if header_button in button.text:
                button.click()
                return

    def click_on_contacts_button(self):
        """
        Переходит на страницу контактов по клику на кнопку "Ещё..." в окне "Контакты"
        """
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(SabyHeaderLocators.BUTTON_CONTACTS),
            f"Couldn't find element by locator {SabyHeaderLocators.BUTTON_CONTACTS}",
        ).click()

        # Ожидаем загрузки новой страницы, так как переходим по click, а не driver.get()
        WebDriverWait(self.driver, 20).until(
            lambda driver: driver.execute_script("return document.readyState")
            == "complete",
            "Page did not load completely",
        )
