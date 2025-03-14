from pages.main_page import MainPage


def test_registry_button(browser):
    page = MainPage(browser)
    page.open()
    assert page.registry_button_is_displayed(), 'Registry button not found.'


def test_offer_button(browser):
    page = MainPage(browser)
    page.open()
    assert page.offer_button_is_displayed(), 'Offer button not found.'


def test_phone_header(browser):
    page = MainPage(browser)
    page.open()
    assert page.phone_header().text == "+7 (8422) 26-09-27", 'Phone not found.'


def test_contacts_footer(browser):
    page = MainPage(browser)
    page.open()
    assert page.contacts_footer().text == "г. Ульяновск, ул. Радищева д. 143\ninfo@aismk.ru\n+7 (8422) 26-09-27", \
        'Contacts not found.'


def test_email_footer(browser):
    page = MainPage(browser)
    page.open()
    assert page.email_footer().text == "support@aismk.ru", 'email not found.'
