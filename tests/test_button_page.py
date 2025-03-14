from pages.simple_button import SimpleButtonPage


def test_button_exist(browser):
    simple_page = SimpleButtonPage(browser)  # Создаем объект класса SimpleButtonPage. Это сессия работы со страницей.
    simple_page.open()  # Открываем страницу методом класса SimpleButtonPage.
    assert simple_page.button_is_displayed(), 'Button not found.'


def test_button_clicked(browser):
    simple_page = SimpleButtonPage(browser)  # Создаем объект класса SimpleButtonPage. Это сессия работы со страницей.
    simple_page.open()  # Открываем страницу методом класса SimpleButtonPage.
    simple_page.button_click()  # Вызываем метод click_button
    assert 'Submitted' == simple_page.result_text

