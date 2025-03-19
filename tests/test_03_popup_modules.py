import time
import pytest

from pages.modules_page import PopupModulesPage
from data.locators.popup_modules_locators import PopupModulesLocators as loc
from data.urls import Urls

urls = Urls()


def test_popup_button(browser):
    """Проверка наличия кнопки открытия попапа"""
    page = PopupModulesPage(browser)
    page.open(urls.MAIN_PAGE)
    assert page.popup_button().is_displayed(), 'Registry button not found.'
    assert page.popup_button().text == "МОДУЛИ", 'Text is not correct.'


def test_popup_open(browser):
    """Проверка открытия попапа"""
    page = PopupModulesPage(browser)
    page.open(urls.MAIN_PAGE)
    page.click_popup_button()
    assert page.find(loc.POPUP_AREA).is_displayed(), 'Popup is not opened.'
    assert page.find(loc.CLOSE_POPUP_BUTTON).is_displayed(), 'Close button is not found.'


def test_popup_close(browser):
    """Проверка закрытия попапа"""
    page = PopupModulesPage(browser)
    page.open(urls.MAIN_PAGE)
    page.click_popup_button()
    page.find(loc.CLOSE_POPUP_BUTTON).click()
    # time.sleep(2)
    assert not page.find(loc.CLOSE_POPUP_BUTTON).is_displayed(), 'Popup is not closed.'


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
    """Проверка перехода на страницу модуля УР из попапа"""
    page = PopupModulesPage(browser)
    page.open(urls.MAIN_PAGE)
    page.click_popup_button()
    assert page.find(module_locator).is_displayed(), 'Module button is not found.'

    page.find(module_locator).click()
    assert browser.current_url == url, 'Wrong url.'
    assert browser.title == title, 'Wrong page title.'
    assert page.find(loc.HEADER_LOCATOR).text == header_text, 'Wrong page header.'
