import allure

from data.urls import Urls

urls = Urls()


@allure.epic('Company site')
@allure.feature('Main page')
@allure.story('01. Check main page items')
@allure.severity(allure.severity_level.CRITICAL)
def test_main_page_items_check(pages):
    page = pages.main
    page.open_main()
    exp = page.EXPECTED_TEXTS

    with allure.step('1. Проверка наличия кнопки перехода на форму обратной связи'):
        assert page.offer_button_is_displayed(), 'Offer button not found.'
        assert page.get_text(page.offer_button()) == exp['offer_button'], 'text not found.'

    with allure.step('2. Проверка наличия телефонного номера'):
        assert page.phone_header_is_displayed(), 'Phone not found.'
        assert page.get_text(page.phone_header()) == exp['phone'], 'Phone not found.'

    with allure.step('3. Проверка наличия контактов в футере сайта'):
        assert page.contacts_footer_is_displayed(), 'Contacts not found.'
        assert page.get_text(page.contacts_footer()) == exp['contacts'], 'Contacts not found.'

    with allure.step('4. Проверка наличия email в футере сайта'):
        assert page.email_footer_is_displayed(), 'email not found.'
        assert page.get_text(page.email_footer()) == exp['email'], 'email not found.'
