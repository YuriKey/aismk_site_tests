import allure
from selenium.webdriver.remote.webelement import WebElement

from data.locators.main_page_locators import MainPageLocators as loc
from data.urls import Urls
from pages.base_page import BasePage

url = Urls()


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    EXPECTED_TEXTS = {
        'offer_button': 'Получить предложение',
        'phone': '+7 (8422) 26-09-27',
        'contacts': 'г. Ульяновск, ул. Радищева д. 143\ninfo@aismk.ru\n+7 (8422) 26-09-27',
        'email': 'support@aismk.ru',
        'url': 'https://aismk.ru/',
        'title': 'Главная — АИСМК - Путь к качеству'
    }

    def open_main(self) -> None:
        with allure.step('Открытие главной страницы'):
            try:
                self.browser.get(url.MAIN_PAGE)
            except Exception as e:
                raise Exception(f'Не удалось открыть главную страницу: {e}')

    def offer_button(self) -> WebElement:
        with allure.step('Поиск кнопки предложения'):
            try:
                return self.find_element(loc.OFFER_BUTTON)
            except Exception as e:
                raise Exception(f'Не удалось найти кнопку предложения на странице: {e}')

    def offer_button_is_displayed(self) -> bool:
        with allure.step('Проверка отображения кнопки предложения'):
            try:
                return self.offer_button().is_displayed()
            except Exception as e:
                raise Exception(f'Кнопка на странице не отображается: {e}')

    def phone_header(self) -> WebElement:
        with allure.step('Поиск телефона в хедере'):
            try:
                return self.find_element(loc.PHONE_HEADER)
            except Exception as e:
                raise Exception(f'Не удалось найти телефон в хедере: {e}')

    def phone_header_is_displayed(self) -> bool:
        with allure.step('Проверка отображения телефона в хедере'):
            try:
                return self.phone_header().is_displayed()
            except Exception as e:
                raise Exception(f'Телефон в хедере не отображается: {e}')

    def contacts_footer(self) -> WebElement:
        with allure.step('Поиск контактов в футере'):
            try:
                return self.find_element(loc.CONTACTS_FOOTER)
            except Exception as e:
                raise Exception(f'Не удалось найти контакты в футере: {e}')

    def contacts_footer_is_displayed(self) -> bool:
        with allure.step('Проверка отображения контактов в футере'):
            try:
                return self.contacts_footer().is_displayed()
            except Exception as e:
                raise Exception(f'Контакты в футере не отображаются: {e}')

    def email_footer(self) -> WebElement:
        with allure.step('Поиск email в футере'):
            try:
                return self.find_element(loc.EMAIL_FOOTER)
            except Exception as e:
                raise Exception(f'Не удалось найти email в футере: {e}')

    def email_footer_is_displayed(self) -> bool:
        with allure.step('Проверка отображения email в футере'):
            try:
                return self.email_footer().is_displayed()
            except Exception as e:
                raise Exception(f'Email в футере не отображается: {e}')
