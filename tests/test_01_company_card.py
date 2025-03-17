import time

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
    page.click_element(locator)  # resolve problem with accept cookies button "if-else" and needless click-function
