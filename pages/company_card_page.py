from pages.base_page import BasePage
from data.locators.company_card_locators import CardPageLocators as loc
from data.urls import Urls

url = Urls()


class CompanyCardPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def company_card_button(self, locator):
        """Метод, который находит кнопку и возвращает элемент."""
        return self.find(locator)

    def company_card_button_is_displayed(self, locator):
        """Метод, который проверяет, отображается ли кнопка. Возвращает True или False."""
        return self.company_card_button(locator).is_displayed()

    def accept_cookies_button(self, locator):
        """Метод, который находит кнопку принятия кукис и возвращает элемент."""
        return self.find(locator)

    def accept_cookies_button_is_displayed(self, locator):
        """Метод, который проверяет, отображается ли кнопка. Возвращает True или False."""
        return self.accept_cookies_button(locator).is_displayed()
