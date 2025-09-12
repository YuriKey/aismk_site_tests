import allure
from selenium.webdriver.remote.webelement import WebElement

from data.locators.popup_modules_locators import PopupModulesLocators as loc
from data.urls import Urls
from pages.base_page import BasePage
from pages.main_page import MainPage

url = Urls()


class ModulesPage(MainPage, BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    EXPECTED_TEXTS = {
        'button_text': 'МОДУЛИ',
        'ur_title': 'Управление рекламациями — АИСМК',
        'ur_text': 'Управление рекламациями',
        'um_title': 'Управление мероприятиями — АИСМК',
        'um_text': 'Управление мероприятиями',
        'sk_title': 'Статистический контроль — АИСМК',
        'sk_text': 'Статистический контроль',
        'mp_title': 'Мониторинг производства — АИСМК',
        'mp_text': 'Мониторинг производства',
        'is_title': 'Информационные стенды — АИСМК',
        'is_text': 'Информационные стенды',
        'ar_title': 'Анализ рисков — АИСМК',
        'ar_text': 'Анализ рисков',
        'vk_title': 'Выборочный контроль — АИСМК',
        'vk_text': 'Выборочный контроль',
        'au_title': 'Аудит — АИСМК',
        'au_text': 'Аудит',
        'akp_title': 'Анализ корневых причин — АИСМК',
        'akp_text': 'Анализ корневых причин',
        'us_title': 'Управление средствами измерений — АИСМК',
        'us_text': 'Управление средствами измерений',
        'offer_button_text': 'Получить предложение',

    }

    def module_button_is_displayed(self, locator, module_name) -> bool:
        with allure.step(f'Проверка отображения кнопки модуля {module_name}'):
            try:
                return self.element_is_displayed(locator)
            except Exception as e:
                raise Exception(f'Ошибка при проверке отображения кнопки модуля {module_name}: {e}')

    def check_current_url(self, expected_url) -> bool:
        with allure.step('Проверка текущего url'):
            try:
                return self.browser.current_url == expected_url
            except Exception as e:
                raise Exception(f'Ошибка при проверке текущего url: {e}')

    def check_page_title(self, expected_title) -> bool:
        with allure.step('Проверка title страницы'):
            try:
                return self.browser.title == expected_title
            except Exception as e:
                raise Exception(f'Ошибка при проверке заголовка страницы: {e}')

    def check_header_text(self, expected_text) -> bool:
        with allure.step('Проверка текста заголовка'):
            try:
                return self.find_element(loc.HEADER_TEXT).text == expected_text
            except Exception as e:
                raise Exception(f'Ошибка при проверке текста заголовка: {e}')

    def check_offer_button(self, expected_text) -> bool:
        with allure.step('Проверка текста кнопки "Получить предложение"'):
            try:
                return self.find_element(loc.OFFER_BUTTON).text == expected_text
            except Exception as e:
                raise Exception(f'Ошибка при проверке кнопки "Получить предложение": {e}')

    def popup_button(self) -> WebElement:
        with allure.step('Поиск кнопки "Модули" в хедере'):
            try:
                return self.find_element(loc.POPUP_BUTTON)
            except Exception as e:
                raise Exception(f'Не удалось найти кнопку "Модули" в хедере: {e}')

    def popup_button_is_displayed(self) -> bool:
        with allure.step('Проверка отображения кнопки "Модули"'):
            try:
                return self.popup_button().is_displayed()
            except Exception as e:
                raise Exception(f'Ошибка при проверке отображения кнопки "Модули": {e}')

    def popup_button_text(self) -> str:
        with allure.step('Получение текста кнопки "Модули"'):
            try:
                return self.popup_button().text
            except Exception as e:
                raise Exception(f'Ошибка при получении текста кнопки "Модули": {e}')

    def click_modules_button(self) -> None:
        with allure.step('Клик по кнопке "Модули"'):
            try:
                self.popup_button().click()
            except Exception as e:
                raise Exception(f'Не удалось кликнуть по кнопке "Модули": {e}')

    def popup_area(self) -> WebElement:
        with allure.step('Поиск области попапа "Модули"'):
            try:
                return self.find_element(loc.POPUP_AREA)
            except Exception as e:
                raise Exception(f'Не удалось найти область попапа "Модули": {e}')

    def popup_area_is_displayed(self) -> bool:
        with allure.step('Проверка отображения области попапа "Модули"'):
            try:
                return self.popup_area().is_displayed()
            except Exception as e:
                raise Exception(f'Ошибка при проверке отображения области попапа "Модули": {e}')

    def popup_close_button(self) -> WebElement:
        with allure.step('Поиск кнопки закрытия попапа "Модули"'):
            try:
                return self.find_element(loc.CLOSE_POPUP_BUTTON)
            except Exception as e:
                raise Exception(f'Не удалось найти кнопку закрытия попапа "Модули": {e}')

    def popup_close_button_is_displayed(self) -> bool:
        with allure.step('Проверка отображения кнопки закрытия попапа "Модули"'):
            try:
                return self.popup_close_button().is_displayed()
            except Exception as e:
                raise Exception(f'Ошибка при проверке отображения кнопки закрытия попапа "Модули": {e}')

    def click_popup_close_button(self) -> None:
        with allure.step('Клик по кнопке закрытия попапа "Модули"'):
            try:
                self.popup_close_button().click()
            except Exception as e:
                raise Exception(f'Не удалось кликнуть по кнопке "Модули": {e}')

    def click_module_button(self, locator) -> None:
        with allure.step('Клик по кнопке модуля'):
            try:
                self.find_element(locator).click()
            except Exception as e:
                raise Exception(f'Не удалось кликнуть по кнопке модуля: {e}')
