import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement

from data.locators.company_card_locators import CardPageLocators as loc
from data.urls import Urls
from pages.base_page import BasePage

url = Urls()


class CompanyCardPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    EXPECTED_TEXTS = {
        'company_info': 'ООО «Алинги»\nЮридический адрес: 432027, Россия, Ульяновская область, г. Ульяновск, '
                        'ул. Радищева д. 143 корп. 4\nОГРН: 1157325005639\nИНН/КПП: 7325139255/732501001\nГенеральный '
                        'директор: Дирксен Алексей Вольдемарович\nДействует на основании Устава\nБанковские '
                        'реквизиты:\nр/с: 40702810129280000903 в Филиал «Нижегородский» АО «АЛЬФА-БАНК»\nБИК '
                        '042202824, к/с 30101810200000000824',
        'url': 'https://aismk.ru/imprint/',
        'title': 'Карточка предприятия — АИСМК'
    }

    def company_card_button(self, locator) -> WebElement:
        with allure.step("Поиск кнопки на странице"):
            try:
                return self.find_element(locator)
            except Exception as e:
                raise Exception(f"Не удалось найти кнопку на странице: {e}")

    def company_card_button_is_displayed(self, locator) -> bool:
        with allure.step("Проверка отображения кнопки на странице"):
            try:
                return self.company_card_button(locator).is_displayed()
            except Exception as e:
                raise Exception(f"Кнопка карточки на странице не отображается: {e}")

    def accept_cookies(self, locator=loc.ACCEPT_COOKIE_BUTTON) -> None:
        with allure.step("Нажатие на кнопку 'Принять cookies'"):
            try:
                if self.element_is_displayed(locator):
                    self.click_element(locator)
            except (NoSuchElementException, TimeoutException):
                pass

    def card_text_area(self) -> object:
        with allure.step("Поиск текстовой области на странице"):
            try:
                return self.find_element(loc.CARD_TEXT_AREA)
            except Exception as e:
                raise Exception(f"Не удалось найти текстовую область на странице: {e}")
