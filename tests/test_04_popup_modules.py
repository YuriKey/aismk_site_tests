import time
import pytest
from pages.modules_page import ModulesPage
from data.locators.popup_modules_locators import PopupModulesLocators as loc
from data.urls import Urls

urls = Urls()


def test_popup_button(browser):
    """Проверка наличия кнопки открытия попапа"""
    page = ModulesPage(browser)
    page.open(urls.MAIN_PAGE)
    assert page.element_is_displayed(loc.POPUP_BUTTON), 'Registry button not found.'
    assert page.find_element(loc.POPUP_BUTTON).text == "МОДУЛИ", 'Text is not correct.'


def test_popup_open(browser):
    """Проверка открытия попапа"""
    page = ModulesPage(browser)
    page.open(urls.MAIN_PAGE)
    page.click_element(loc.POPUP_BUTTON)
    assert page.element_is_displayed(loc.POPUP_AREA), 'Popup is not opened.'
    assert page.element_is_displayed(loc.CLOSE_POPUP_BUTTON), 'Close button is not found.'


def test_popup_close(browser):
    """Проверка закрытия попапа"""
    page = ModulesPage(browser)
    page.open(urls.MAIN_PAGE)
    page.click_element(loc.POPUP_BUTTON)
    page.click_element(loc.CLOSE_POPUP_BUTTON)
    time.sleep(1)
    assert not page.element_is_displayed(loc.CLOSE_POPUP_BUTTON), 'Popup is not closed.'


@pytest.mark.parametrize('module_locator, url, title, header_text', [
    (loc.POPUP_UR, urls.MODULE_UR, "Управление рекламациями — АИСМК", "Управление рекламациями"),
    (loc.POPUP_UM, urls.MODULE_UM, "Управление мероприятиями — АИСМК", "Управление мероприятиями"),
    (loc.POPUP_SK, urls.MODULE_SK, "Статистический контроль — АИСМК", "Статистический контроль"),
    (loc.POPUP_MP, urls.MODULE_MP, "Мониторинг производства — АИСМК", "Мониторинг производства"),
    (loc.POPUP_IS, urls.MODULE_IS, "Информационные стенды — АИСМК", "Информационные стенды"),
    (loc.POPUP_AR, urls.MODULE_AR, "Анализ рисков — АИСМК", "Анализ рисков"),
    (loc.POPUP_VK, urls.MODULE_VK, "Выборочный контроль — АИСМК", "Выборочный контроль"),
    (loc.POPUP_AU, urls.MODULE_AU, "Аудит — АИСМК", "Аудит"),
    (loc.POPUP_AKP, urls.MODULE_AKP, "Анализ корневых причин — АИСМК", "Анализ корневых причин")
])
def test_popup_module_following(browser, module_locator, url, title, header_text):
    """Проверка перехода на страницу модуля из попапа с помощью soft assert."""
    page = ModulesPage(browser)
    page.open(urls.MAIN_PAGE)
    page.click_element(loc.POPUP_BUTTON)

    errors = []

    page.wait_for_visibility(module_locator, errors, f'Module button "{module_locator}" is not found')

    page.click_element(module_locator)

    page.check_current_url(url, errors)
    page.check_page_title(title, errors)
    page.check_header_text(loc.HEADER_TEXT, header_text, errors)
    page.check_offer_button(loc.OFFER_BUTTON, "Получить предложение", errors)

    assert not errors, "\n".join(errors)
