from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SabyHomePageLocators:
    BUTTON_CONTACTS_HEADER = (
        By.XPATH,
        '//div[@class="sbisru-Header__menu-link sbis_ru-Header__menu-link sbisru-Header__menu-link--hover" and text()="Контакты"]',
    )

    BUTTON_CONTACTS = (
        By.CSS_SELECTOR,
        "a[href='/contacts'].sbisru-link.sbis_ru-link",
    )


# noinspection SpellCheckingInspection
class SabyHomePage(BasePage):
    PAGE_URL = "https://sbis.ru"

    def click_on_contacts_header(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(SabyHomePageLocators.BUTTON_CONTACTS_HEADER),
            f"Couldn't find element by locator {SabyHomePageLocators.BUTTON_CONTACTS_HEADER}",
        ).click()

    def click_on_contacts_button(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(SabyHomePageLocators.BUTTON_CONTACTS),
            f"Couldn't find element by locator {SabyHomePageLocators.BUTTON_CONTACTS}",
        ).click()

        # Ожидаем загрузки новой страницы, так как переходим по click, а не driver.get()
        WebDriverWait(self.driver, 20).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete',
            "Page did not load completely"
        )
