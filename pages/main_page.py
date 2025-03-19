from pages.base_page import BasePage
from data.locators.main_page_locators import MainPageLocators as loc
from data.urls import Urls

url = Urls()


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_main(self):
        """Метод, который открывает главную страницу."""
        self.browser.get(url.MAIN_PAGE)

    def offer_button(self):
        """Метод, который находит кнопку на форму обратной связи и возвращает элемент кнопки."""
        return self.find(loc.OFFER_BUTTON)

    def offer_button_is_displayed(self):
        """Метод, который проверяет, отображается ли кнопка. Возвращает True или False."""
        return self.offer_button().is_displayed()

    def phone_header(self):
        """Метод, который находит телефон и возвращает элемент."""
        return self.find(loc.PHONE_HEADER)

    def phone_header_is_displayed(self):
        """Метод, который проверяет, отображается ли кнопка. Возвращает True или False."""
        return self.phone_header().is_displayed()

    def contacts_footer(self):
        """Метод, который находит контакты и возвращает элемент."""
        return self.find(loc.CONTACTS_FOOTER)

    def contacts_footer_is_displayed(self):
        """Метод, который проверяет, отображается ли кнопка. Возвращает True или False."""
        return self.contacts_footer().is_displayed()

    def email_footer(self):
        """Метод, который находит email и возвращает элемент."""
        return self.find(loc.EMAIL_FOOTER)

    def email_footer_is_displayed(self):
        """Метод, который проверяет, отображается ли кнопка. Возвращает True или False."""
        return self.email_footer().is_displayed()
