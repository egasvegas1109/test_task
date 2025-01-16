from pages.tensor_about_page import TensorAboutPage
from pages.tensor_home_page import TensorHomePage
from pages.saby_home_page import SabyHomePage
from pages.saby_contacts import SabyContactsPage
from conftest import create_web_driver


# noinspection SpellCheckingInspection
def test_banner_navigation_and_elements(create_web_driver):
    #Создание экземпляров классов,
    #можно вынести в отдельную фикстуру, но тогда будут создаваться и объекты,
    #которые не нужны в данном тесте например
    saby_home_page = SabyHomePage(create_web_driver)
    saby_contacts = SabyContactsPage(create_web_driver)
    tensor_home_page = TensorHomePage(create_web_driver)
    tensor_about_page = TensorAboutPage(create_web_driver)

    saby_home_page.go_to_site()
    saby_home_page.click_on_contacts_header()
    saby_home_page.click_on_contacts_button()
    saby_contacts.click_on_tensor_banner()

    assert tensor_home_page.check_block_power_in_people_exist() == True
    tensor_home_page.power_in_people_click_button()
    assert tensor_home_page.get_current_url() == "https://tensor.ru/about"

    assert tensor_about_page.are_images_same_size_from_work_section() == True

# noinspection SpellCheckingInspection
def test_region_detection_and_change(create_web_driver):
    saby_home_page = SabyHomePage(create_web_driver)
    saby_contacts = SabyContactsPage(create_web_driver)

    saby_home_page.go_to_site()
    saby_home_page.click_on_contacts_header()
    saby_home_page.click_on_contacts_button()

    assert saby_contacts.check_region_selector_exist('Ярославская') == True
    assert saby_contacts.check_partners_list_exist() == True

    yar_partners_list = saby_contacts.get_partners_list()

    saby_contacts.set_region('Камчатский край')
    assert saby_contacts.check_region_selector_exist('Камчатский край') == True

    kamch_partners_list = saby_contacts.get_partners_list()
    assert yar_partners_list != kamch_partners_list

    current_title = saby_contacts.get_current_title()
    current_url = saby_contacts.get_current_url()
    assert 'Камчатский край' in current_title
    assert '41-kamchatskij-kraj' in current_url

