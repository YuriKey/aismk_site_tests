import allure

from data.locators.rosregistry_locators import RegistryPageLocators as loc
from data.urls import Urls
from pages.base_page import BasePage
from pages.main_page import MainPage

url = Urls()


class RegistryPage(MainPage, BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    EXPECTED_TEXTS = {
        'owner_title': 'Общество с ограниченной ответственностью "Алинги"',
        'owner_short_title': 'ООО "Алинги"',
        'soft_full_title': 'Автоматизированная Информационная Система Менеджмента Качества',
        'title': 'АИСМК',
        'url': 'https://reestr.digital.gov.ru/reestr/1284851/'
    }

    def registry_button(self):
        with allure.step('Поиск кнопки перехода на Росреестр'):
            try:
                return self.find_element(loc.REGISTRY_BUTTON)
            except Exception as e:
                raise Exception(f'Кнопка перехода на Росреестр не найдена: {e}')

    def registry_button_is_displayed(self) -> bool:
        with allure.step('Проверка отображения кнопки перехода на Росреестр'):
            try:
                return self.registry_button().is_displayed()
            except Exception as e:
                raise Exception(f'Кнопка перехода на Росреестр не отображается: {e}')

    def click_registry_button(self):
        with allure.step('Нажатие на кнопку перехода на Росреестр'):
            try:
                self.registry_button().click()
            except Exception as e:
                raise Exception(f'Не удалось нажать на кнопку перехода на Росреестр: {e}')


