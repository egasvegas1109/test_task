from components.saby_footer_component import SabyFooter
from components.saby_header_component import SabyHeader
from pages.base_page import BasePage


# noinspection SpellCheckingInspection
class SabyHomePage(BasePage):
    PAGE_URL = "https://saby.ru"

    def __init__(self, driver):
        super().__init__(driver)
        self.header = SabyHeader(driver)  # Используем композицию (PageComponent)
        self.footer = SabyFooter(driver)  # Используем композицию (PageComponent)
