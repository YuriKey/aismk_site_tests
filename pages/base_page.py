"""
Хранит свойства и методы, присущие всем страницам.
"""


class BasePage:
    def __init__(self, browser):
        self.browser = browser  # Браузер, принадлежащий классу BasePage равен переданному браузеру.

    def open(self, url):  # Метод, который открывает страницу.
        self.browser.get(url)

    def find_item(self, args):  # Принимает любые аргументы
        return self.browser.find_element(*args)  # И ищет элемент.

    def click_element(self, args):
        return self.find_item(args).click()

    def fill_field(self, args, text):
        return self.find_item(args).send_keys(text)

    def element_is_displayed(self, args):
        return self.find_item(args).is_displayed()
