"""
Хранит свойства и методы, присущие всем страницам.
"""
from data.urls import Urls
url = Urls()


class BasePage:
    def __init__(self, browser):
        self.browser = browser  # Браузер, принадлежащий классу BasePage равен переданному браузеру.

    def open(self):  # Метод, который открывает страницу.
        self.browser.get(url.MAIN_PAGE_URL)

    def find(self, args):  # Давай любые аргументы.
        return self.browser.find_element(*args)  # А я найду элемент.

    def click(self, args):
        return self.find(args).click()  # А я кликну на элемент.

    def fill(self, args, text):
        return self.find(args).send_keys(text)  # А я запишу туда текст.

    # def element_is_displayed(self, args):
    #     return self.find(args).is_displayed()



