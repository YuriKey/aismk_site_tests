from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data.urls import Urls
from pages.base_page import BasePage

url = Urls()


class ModulesPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def assertion_text_func(self, locator, expected):
        """Метод, который сравнивает ожидаемый и фактический текст на странице."""
        actual = self.find_item(locator).text
        assert expected == actual, f"Text '{actual}' is not correct."

    def wait_for_visibility(self, locator, errors, error_message):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(locator))
        except TimeoutException:
            errors.append(error_message)

    def check_current_url(self, expected_url, errors):
        if self.browser.current_url != expected_url:
            errors.append(f'Wrong url. Expected {expected_url}, but got {self.browser.current_url}')

    def check_page_title(self, expected_title, errors):
        if self.browser.title != expected_title:
            errors.append(f'Wrong page title. Expected {expected_title}, but got {self.browser.title}')

    def check_header_text(self, locator, expected_text, errors):
        element = self.find_item(locator)
        if element.text != expected_text:
            errors.append(f'Wrong page header. Expected "{expected_text}", but got "{element.text}"')

    def check_offer_button(self, locator, expected_text, errors):
        try:
            button = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(locator))
            if button.text != expected_text:
                errors.append(f'Wrong text of offer button. Expected "{expected_text}", but got "{button.text}"')
        except TimeoutException:
            errors.append('Offer button not found')