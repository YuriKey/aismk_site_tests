from pages.base_page import BasePage
from data.locators.popup_modules_locators import PopupModulesLocators as loc
from data.urls import Urls

url = Urls()


class PopupModulesPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def popup_button(self):
        """Метод, который находит кнопку для открытия попапа с модулями"""
        return self.find(loc.POPUP_BUTTON)

    def popup_button_is_displayed(self):
        """Метод, который проверяет отображение кнопки для открытия попапа"""
        return self.popup_button().is_displayed()

    def click_popup_button(self):
        """Метод, который открывает попап с модулями"""
        self.popup_button().click()

    def assertion_text_func(self, locator, expected):
        """Метод, который сравнивает ожидаемый и фактический текст на странице."""
        actual = self.find(locator).text
        assert expected == actual, f"Text '{actual}' is not correct."

