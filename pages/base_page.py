from selenium.webdriver.safari.webdriver import WebDriver


class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def go_to_site(self):
        """
        Переходит по URL, указанному в данном PageObject.
        """
        return self.driver.get(self.PAGE_URL)

    def get_current_url(self):
        """
        Возвращает текущий URL.
        """
        return self.driver.current_url

    def get_current_title(self):
        """
        Возвращает заголовок страницы.
        """
        return self.driver.title
