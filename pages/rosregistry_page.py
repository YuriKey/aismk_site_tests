from pages.base_page import BasePage
from data.locators.rosregistry_locators import RegistryPageLocators as loc
from data.urls import Urls

url = Urls()


class RegistryPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def registry_button(self):
        """Метод, который находит кнопку registry_button и возвращает элемент кнопки."""
        return self.find(loc.REGISTRY_BUTTON)

    def registry_button_is_displayed(self):
        """Метод, который проверяет, отображается ли кнопка. Возвращает True или False."""
        return self.registry_button().is_displayed()

    def click_registry_button(self):
        """Метод, который кликает по кнопке."""
        self.registry_button().click()

    def assertion_text_func(self, locator, expected):
        """Метод, который сравнивает ожидаемый и фактический текст на странице."""
        actual = self.find(locator).text
        assert expected == actual, f"Text '{actual}' is not correct."
