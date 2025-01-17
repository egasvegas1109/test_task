from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TensorAboutPageLocators:
    IMG_FROM_WORK_SECTION = (
        By.CSS_SELECTOR,
        "img.tensor_ru-About__block3-image.new_lazy",
    )


# noinspection SpellCheckingInspection
class TensorAboutPage(BasePage):
    PAGE_URL = "https://tensor.ru/about"

    def are_images_same_size_from_work_section(self):
        """
        Проверяет одинаковый ли размер у изображений в разделе "Работаем"
        """
        # Находим все изображения
        images = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                TensorAboutPageLocators.IMG_FROM_WORK_SECTION
            ),
            f"Couldn't find elements by locator {TensorAboutPageLocators.IMG_FROM_WORK_SECTION}",
        )

        # Прокрутка до них, чтобы вызвалось событие load
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", images[0]
        )

        # Дожидаемся полной загрузки каждого изображения
        for image in images:
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.execute_script(
                    "return arguments[0].complete && arguments[0].naturalWidth > 0;",
                    image,
                ),
                f"Image {image.get_attribute('src')} did not load",
            )

        first_image_width = images[0].get_attribute("width")
        first_image_height = images[0].get_attribute("height")

        for image in images[1:]:
            image_width = image.get_attribute("width")
            image_height = image.get_attribute("height")

            if image_width != first_image_width or image_height != first_image_height:
                return False

        return True
