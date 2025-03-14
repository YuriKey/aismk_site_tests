from selenium import webdriver
import pytest


@pytest.fixture(scope='session')  # scope='session' один раз запускаем браузер для всех тестов в файле
def browser():
    chrome_browser = webdriver.Chrome()  # создаем экземпляр браузера
    chrome_browser.implicitly_wait(10)  # ждем 10 секунд пока не найдет элемент
    return chrome_browser  # возвращаем браузер








