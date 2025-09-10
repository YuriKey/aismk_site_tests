import allure
import pytest

from data.urls import Urls

urls = Urls()


@allure.epic('Company site')
@allure.feature('Main page')
@allure.story('00. Check main page open')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('url', [
    urls.MAIN_PAGE,
    urls.ALINGHI_URL,
    urls.RF_URL
])
def test_site_open(pages, url):
    page = pages.main
    page.open(url)
    exp = page.EXPECTED_TEXTS

    with allure.step('1. Проверка открытия страницы'):
        assert page.get_current_url() == exp['url'], 'Site isn`t open'
        assert page.get_title() == exp['title'], 'Wrong title'
