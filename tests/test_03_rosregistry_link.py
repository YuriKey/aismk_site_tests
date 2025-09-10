from pages.rosregistry_page import RegistryPage
from data.locators.rosregistry_locators import RegistryPageLocators as loc
from data.urls import Urls

urls = Urls()


def test_rosregistry_button(browser):
    """Проверка наличия кнопки перехода на запись в росреестре"""
    page = RegistryPage(browser)
    page.open(urls.MAIN_PAGE)
    assert page.registry_button_is_displayed(), 'Registry button not found.'
    assert page.registry_button().text == "В РЕЕСТРЕ РОССИЙСКОГО ПО", 'Text is not correct.'


def test_check_following(browser):
    """Проверка перехода на запись в Росреестре по клику на кнопку.
    Проверка данных страницы росреестра.
    """
    page = RegistryPage(browser)
    page.open(urls.MAIN_PAGE)

    page.click_registry_button()

    test_data = [
        (loc.OWNER_TITLE, 'Общество с ограниченной ответственностью "Алинги"'),
        (loc.OWNER_SHORT_TITLE, 'ООО "Алинги"'),
        (loc.HEADER_TITLE, "АИСМК"),
        (loc.SOFT_FULL_TITLE, "Автоматизированная Информационная Система Менеджмента Качества")
    ]

    assert browser.current_url == urls.RR_SOFTWARE_PAGE, 'Incorrect URL'
    assert browser.title == "АИСМК"

    for locator, expected in test_data:
        page.assertion_text_func(locator, expected)
