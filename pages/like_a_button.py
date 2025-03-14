"""
Это дочерний класс от класса BasePage. Ему доступны все методы класса BasePage и методы, описанные в нем.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


button_selector = (By.LINK_TEXT, 'Click')
result_selector = (By.ID, 'result-text')


class LikeAButton(BasePage):
    def __init__(self, browser):
        super().__init__(browser)  # Передаем браузер в родительский класс.

    def open(self):  # Метод, который открывает страницу.
        self.browser.get('https://www.qa-practice.com/elements/button/like_a_button')

    @property
    def button(self):  # Метод, который находит кнопку и возвращает элемент кнопки.
        return self.find(button_selector)

    @property
    def button_is_displayed(self):  # Метод, который проверяет, отображается ли кнопка. Возвращает True или False.
        return self.button.is_displayed()

    def button_click(self):  # Метод, который кликает по кнопке.
        self.button.click()

    @property
    def result(self):  # Метод, который находит текстовое поле с результатом и возвращает это поле.
        return self.find((By.ID, 'result-text'))

    @property  # С помощью декоратора @property мы можем вызывать этот метод как атрибут класса, т.е без скобок.
    def result_text(self):  # Метод, который возвращает текст из текстового поля с результатом.
        return self.result.text


