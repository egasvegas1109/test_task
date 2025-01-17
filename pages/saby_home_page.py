from components.saby_header_component import SabyHeader
from pages.base_page import BasePage

class SabyHomePageLocators:
    pass

# noinspection SpellCheckingInspection
class SabyHomePage(BasePage):
    PAGE_URL = "https://sbis.ru"

    def __init__(self, driver):
        super().__init__(driver)
        self.header = SabyHeader(driver) #Используем композицию (PageComponent)
