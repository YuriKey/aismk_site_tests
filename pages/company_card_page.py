from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException, TimeoutException
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

    def accept_cookies(self, locator=loc.ACCEPT_COOKIE_BUTTON):
        """Метод, который принимает куки, если кнопка отображается."""
        try:
            if self.find(locator).is_displayed():
                self.click_element(locator)
        except (NoSuchElementException, TimeoutException):
            pass
