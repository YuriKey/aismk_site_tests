import allure
import pytest

from data.locators.company_card_locators import CardPageLocators as loc
from data.urls import Urls

urls = Urls()


@allure.epic('Company site')
@allure.feature('Company page')
@allure.story('02. Check company card page')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('locator', [
    loc.COMPANY_CARD_BUTTON,
    loc.COMPANY_CARD_BUTTON_FOOTER
])
def test_check_company_card_page(pages, locator):
    page = pages.main
    c_page = pages.company
    page.open_main()
    exp = c_page.EXPECTED_TEXTS

    with allure.step('1. Проверка отображения ссылки на карточку предприятия'):
        assert c_page.company_card_button_is_displayed(locator), \
            'Карточка предприятия не отображается'

        c_page.accept_cookies()

    with allure.step('2. Переход на карточку предприятия'):
        page.click_element(locator)

    with allure.step('3. Проверка корректности отображения информации о компании'):
        assert page.get_current_url() == exp['url'], \
            'Не верный url страницы карточки предприятия'
        assert page.get_title() == exp['title'], \
            'не верный title страницы карточки предприятия'
        assert page.get_text(c_page.card_text_area()) == exp['company_info'], \
            'Не верный текст информации о компании'
