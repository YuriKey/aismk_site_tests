import allure

from data.locators.buttons_modules_locators import PopupModulesLocators as loc
from data.urls import Urls

urls = Urls()


@allure.epic('Company site')
@allure.feature('Modules')
@allure.story('04. Popup modules open')
@allure.severity(allure.severity_level.NORMAL)
def test_popup_open(pages):
    page = pages.modules
    page.open_main()
    exp = page.EXPECTED_TEXTS

    with allure.step('1. Проверка отображения кнопки открытия попапа'):
        assert page.popup_button_is_displayed(), \
            'Кнопка открытия попапа модулей не найдена'
        assert page.popup_button_text() == exp['button_text'], \
            'Текст кнопки открытия попапа модулей не соответствует ожидаемому'

    with allure.step('2. Проверка открытия попапа'):
        page.click_modules_button()
        assert page.popup_area_is_displayed(), \
            'Попап не открыт'
        assert page.popup_close_button_is_displayed(), \
            'Кнопка закрытия попапа не найдена'

    with allure.step('3. Проверка закрытия попапа'):
        page.click_popup_close_button()
        assert not page.element_is_displayed(loc.CLOSE_POPUP_BUTTON), \
            'Попап не закрыт'
