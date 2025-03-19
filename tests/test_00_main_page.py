import pytest
from pages.main_page import MainPage
from data.urls import Urls

urls = Urls()


@pytest.mark.parametrize('url', [
    urls.MAIN_PAGE,
    urls.ALINGHI_URL,
    urls.RF_URL
])
def test_site_open(browser, url):
    page = MainPage(browser)
    page.open(url)
    assert page.browser.current_url == 'https://aismk.ru/', 'Site isn`t open'
    assert page.browser.title == "Главная — АИСМК - Путь к качеству", 'Wrong title'


def test_offer_button(browser):
    """Проверка наличия кнопки перехода на форму обратной связи"""
    page = MainPage(browser)
    page.open_main()
    assert page.offer_button_is_displayed(), 'Offer button not found.'
    assert page.offer_button().text == "Получить предложение", 'text not found.'


def test_phone_header(browser):
    """Проверка наличия номера телефона в шапке сайта"""
    page = MainPage(browser)
    page.open_main()
    assert page.phone_header_is_displayed(), 'Phone not found.'
    assert page.phone_header().text == "+7 (8422) 26-09-27", 'Phone not found.'


def test_contacts_footer(browser):
    """Проверка наличия контактов в подвале сайта"""
    page = MainPage(browser)
    page.open_main()
    assert page.contacts_footer_is_displayed(), 'Contacts not found.'
    assert page.contacts_footer().text == "г. Ульяновск, ул. Радищева д. 143\ninfo@aismk.ru\n+7 (8422) 26-09-27", \
        'Contacts not found.'


def test_email_footer(browser):
    """Проверка наличия контактов в подвале сайта"""
    page = MainPage(browser)
    page.open_main()
    assert page.email_footer_is_displayed(), 'email not found.'
    assert page.email_footer().text == "support@aismk.ru", 'email not found.'
