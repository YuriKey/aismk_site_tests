import allure
import pytest

from data.locators.buttons_modules_locators import PopupModulesLocators as loc
from pages.modules_page import ModulesPage as mp
from data.urls import Urls

urls = Urls()

exp = mp.EXPECTED_TEXTS


@allure.epic('Company site')
@allure.feature('Modules')
@allure.story('05. Popup modules following')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize('module_locator, url, title, header_text', [
    (loc.POPUP_UR, urls.MODULE_UR, exp['ur_title'], exp['ur_text']),
    (loc.POPUP_UM, urls.MODULE_UM, exp['um_title'], exp['um_text']),
    (loc.POPUP_SK, urls.MODULE_SK, exp['sk_title'], exp['sk_text']),
    (loc.POPUP_MP, urls.MODULE_MP, exp['mp_title'], exp['mp_text']),
    (loc.POPUP_IS, urls.MODULE_IS, exp['is_title'], exp['is_text']),
    (loc.POPUP_AR, urls.MODULE_AR, exp['ar_title'], exp['ar_text']),
    (loc.POPUP_VK, urls.MODULE_VK, exp['vk_title'], exp['vk_text']),
    (loc.POPUP_AU, urls.MODULE_AU, exp['au_title'], exp['au_text']),
    (loc.POPUP_AKP, urls.MODULE_AKP, exp['akp_title'], exp['akp_text']),
    (loc.POPUP_US, urls.MODULE_US, exp['us_title'], exp['us_text'])
])
def test_popup_module_following(pages, module_locator, url, title, header_text):
    page = pages.modules
    page.open_main()
    page.click_modules_button()

    with allure.step(f'1. Проверить отображение кнопки модуля "{header_text}" в области попапа'):
        assert page.module_button_is_displayed(module_locator, header_text), \
            f'Кнопка модуля "{header_text}" не найдена'

    with allure.step(f'2. Перейти на страницу модуля "{header_text}"'):
        page.click_module_button(module_locator)

    with allure.step(f'3. Проверить url страницы модуля "{header_text}"'):
        assert page.check_current_url(url), \
            f'Url страницы модуля "{header_text}" не совпадает с ожидаемым: {url}'

    with allure.step(f'4. Проверить title страницы модуля "{header_text}"'):
        assert page.check_page_title(title), \
            f'Title страницы модуля "{header_text}" не совпадает с ожидаемым: {title}'

    with allure.step(f'5. Проверить текст заголовка страницы модуля "{header_text}"'):
        assert page.check_header_text(header_text), \
            f'Текст заголовка страницы модуля "{header_text}" не совпадает с ожидаемым: {header_text}'

    with allure.step(f'6. Проверить отображение кнопки "Получить предложение" на странице модуля "{header_text}"'):
        assert page.check_offer_button(exp['offer_button_text']), \
            f'Кнопка "Получить предложение" на странице модуля "{header_text}" не найдена'
