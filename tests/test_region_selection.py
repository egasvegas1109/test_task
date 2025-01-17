from pages.saby_home_page import SabyHomePage
from pages.saby_contacts_page import SabyContactsPage
from conftest import create_web_driver


# noinspection SpellCheckingInspection
def test_region_detection_and_change(create_web_driver):
    saby_home_page = SabyHomePage(create_web_driver)
    saby_contacts = SabyContactsPage(create_web_driver)

    saby_home_page.go_to_site()
    saby_home_page.header.click_on_button_header("Контакты")
    saby_home_page.header.click_on_contacts_button()

    assert saby_contacts.check_region_selector_exist("Ярославская") == True
    yar_partners_list = saby_contacts.get_partners_list()
    assert yar_partners_list

    saby_contacts.set_region("Камчатский край")
    assert saby_contacts.check_region_selector_exist("Камчатский край") == True

    kamch_partners_list = saby_contacts.get_partners_list()
    assert yar_partners_list != kamch_partners_list

    current_title = saby_contacts.get_current_title()
    current_url = saby_contacts.get_current_url()
    assert "Камчатский край" in current_title
    assert "41-kamchatskij-kraj" in current_url
