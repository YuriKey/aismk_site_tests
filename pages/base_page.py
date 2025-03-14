"""
Хранит свойства и методы, присущие всем страницам.
"""


class BasePage:
    def __init__(self, browser):
        self.browser = browser  # Браузер, принадлежащий классу BasePage равен переданному браузеру.

    def find(self, args):  # Давай любые аргументы.
        """
        Эта функция доступна для все экземпляров страниц
        """
        return self.browser.find_element(*args)  # А я найду элемент.


