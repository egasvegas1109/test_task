from pages.saby_download import SabyDownloadPage
from pages.saby_home_page import SabyHomePage
from conftest import create_web_driver


# noinspection SpellCheckingInspection
def test_download_plugin_sbis_and_size(create_web_driver):
    saby_home_page = SabyHomePage(create_web_driver)
    saby_download_page = SabyDownloadPage(create_web_driver)

    saby_home_page.go_to_site()
    saby_home_page.footer.click_on_button_footer("Скачать локальные версии")
    saby_download_page.set_operating_system("Windows")
    saby_download_page.set_product_download("Saby Plugin")
    saby_download_page.download_product_web_version()
