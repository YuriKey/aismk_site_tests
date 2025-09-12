import allure

from data.locators.rosregistry_locators import RegistryPageLocators as loc
from data.urls import Urls

urls = Urls()


@allure.epic('Company site')
@allure.feature('Rosregistry page')
@allure.story('03. Rosregistry following check')
@allure.severity(allure.severity_level.NORMAL)
def test_rosregistry_link(pages):
    page = pages.registry
    page.open_main()
    exp = page.EXPECTED_TEXTS

    test_data = [
        (loc.OWNER_TITLE, exp['owner_title']),
        (loc.OWNER_SHORT_TITLE, exp['owner_short_title']),
        (loc.HEADER_TITLE, exp['title']),
        (loc.SOFT_FULL_TITLE, exp['soft_full_title']),
    ]

    with allure.step('1. Проверка наличия кнопки перехода на запись в Росреестре'):
        assert page.registry_button_is_displayed(), \
            'Кнопка перехода на запись в росреестре не отображается'

    with allure.step('2. Нажать на кнопку перехода на запись в Росреестре'):
        page.click_registry_button()
        assert page.get_current_url() == exp['url'], \
            'Не верный url страницы'
        assert page.get_title() == exp['title'], \
            'Не верный title страницы'

    with allure.step('3. Проверка данных страницы Росреестра'):
        for locator, expected in test_data:
            page.assertion_text_func(locator, expected)
