import pytest
from pages.company_card_page import CompanyCardPage
from data.locators.company_card_locators import CardPageLocators as loc
from data.urls import Urls

urls = Urls()


@pytest.mark.parametrize('locator, expected_text', [
    (loc.COMPANY_CARD_BUTTON, "Карточка предприятия"),
    (loc.COMPANY_CARD_BUTTON_FOOTER, "КАРТОЧКА ПРЕДПРИЯТИЯ")
])
def test_company_card_button_exists(browser, locator, expected_text):
    page = CompanyCardPage(browser)
    page.open(urls.MAIN_PAGE)
    assert page.company_card_button_is_displayed(locator), 'Company card button not found.'
    assert page.company_card_button(locator).text == expected_text, 'text not found.'


@pytest.mark.parametrize('locator', [
    loc.COMPANY_CARD_BUTTON,
    loc.COMPANY_CARD_BUTTON_FOOTER
])
def test_check_following(browser, locator):
    page = CompanyCardPage(browser)
    page.open(urls.MAIN_PAGE)

    page.accept_cookies()

    page.click_element(locator)
    actual_text = page.find(loc.CARD_TEXT_AREA).text
    assert browser.current_url == urls.COMPANY_CARD_PAGE, 'Incorrect url'
    assert browser.title == "Карточка предприятия — АИСМК", 'Incorrect title'
    assert actual_text == ("ООО «Алинги»\nЮридический адрес: 432027, Россия, Ульяновская область, г. Ульяновск, "
                           "ул. Радищева д. 143 корп. 4\nОГРН: 1157325005639\nИНН/КПП: "
                           "7325139255/732501001\nГенеральный директор: Дирксен Алексей Вольдемарович\nДействует на "
                           "основании Устава\nБанковские реквизиты:\nр/с: 40702810129280000903 в Филиал "
                           "«Нижегородский» АО «АЛЬФА-БАНК»\nБИК 042202824, к/с 30101810200000000824"), ('Incorrect '
                                                                                                         'company info')


