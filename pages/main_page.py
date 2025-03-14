from pages.base_page import BasePage
from data.locators.main_page_locators import MainPageLocators as loc


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def registry_button(self):
        """Метод, который находит кнопку registry_button и возвращает элемент кнопки registry_button"""
        return self.find(loc.REGISTRY_BUTTON)

    def registry_button_is_displayed(self):
        """Метод, который проверяет, отображается ли кнопка. Возвращает True или False."""
        return self.registry_button().is_displayed()

    def offer_button(self):
        """Метод, который находит ссылку и возвращает элемент кнопки."""
        return self.find(loc.OFFER_BUTTON)

    def offer_button_is_displayed(self):
        """Метод, который проверяет, отображается ли кнопка. Возвращает True или False."""
        return self.offer_button().is_displayed()

    def phone_header(self):
        """Метод, который находит телефон и возвращает элемент."""
        return self.find(loc.PHONE_HEADER)

    def contacts_footer(self):
        """Метод, который находит контакты и возвращает элемент."""
        return self.find(loc.CONTACTS_FOOTER)

    def email_footer(self):
        """Метод, который находит email и возвращает элемент."""
        return self.find(loc.EMAIL_FOOTER)