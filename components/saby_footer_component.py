from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SabyFooterLocators:
    BUTTONS_FOOTER = (By.CSS_SELECTOR, "a.sbisru-Footer__link")


# noinspection SpellCheckingInspection
class SabyFooter(BasePage):
    def click_on_button_footer(self, footer_button: str):
        """
        Кликает на указанную кнопку в footer.
        :param footer_button: название кнопки
        """
        footer_buttons = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(SabyFooterLocators.BUTTONS_FOOTER),
            f"Couldn't find element by locator {SabyFooterLocators.BUTTONS_FOOTER}",
        )

        for button in footer_buttons:
            if footer_button in button.text:
                button.click()
                break
