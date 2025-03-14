from selenium.webdriver.common.by import By
from pages.base_page import BasePage

registry_button_selector = (By.XPATH, '//*[@class="elementor-button-icon elementor-align-icon-left"]')
offer_button_selector = (By.XPATH, '//*[@class="elementor-button-link elementor-button elementor-size-md"]')
phone_header_selector = (By.XPATH, '//*[@class="elementor-heading-title elementor-size-default"][contains(text(),'
                                   '"+7 (8422) 26-09-27")]')
contacts_footer_selector = (By.XPATH, '//*[@class="elementor-heading-title elementor-size-default"][contains(text(),'
                                      '"Радищева")]')
email_footer_selector = (By.XPATH, '//*[@class="elementor-heading-title elementor-size-default"][contains(text(),'
                                   '"support@aismk.ru")]')


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def registry_button(self):  # Метод, который находит кнопку registry_button_selector и возвращает элемент кнопки.
        return self.find(registry_button_selector)

    def registry_button_is_displayed(self):
        """Метод, который проверяет, отображается ли кнопка. Возвращает True или False."""
        return self.registry_button().is_displayed()

    def offer_button(self):
        """Метод, который находит ссылку и возвращает элемент кнопки."""
        return self.find(registry_button_selector)

    def offer_button_is_displayed(self):
        """Метод, который проверяет, отображается ли кнопка. Возвращает True или False."""
        return self.offer_button().is_displayed()

    def phone_header(self):
        """Метод, который находит телефон и возвращает элемент."""
        return self.find(phone_header_selector)

    def contacts_footer(self):
        """Метод, который находит контакты и возвращает элемент."""
        return self.find(contacts_footer_selector)

    def email_footer(self):
        """Метод, который находит email и возвращает элемент."""
        return self.find(email_footer_selector)