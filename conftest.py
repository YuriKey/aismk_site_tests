import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

from pages.page_factory import PageFactory


@pytest.fixture(scope='session')
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_browser = webdriver.Chrome(options=chrome_options)
    chrome_browser.implicitly_wait(3)
    yield chrome_browser
    chrome_browser.quit()


@pytest.fixture
def pages(browser):
    with allure.step('Инициализация страницы'):
        return PageFactory(browser)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = None

        for fixture_name in item.fixturenames:
            fixture = item.funcargs.get(fixture_name)

            if hasattr(fixture, 'driver'):
                driver = fixture.driver
                break
            elif hasattr(fixture, 'browser'):
                driver = fixture.browser
                break
            elif isinstance(fixture, WebDriver):
                driver = fixture
                break

        if driver:
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"screenshot_{item.nodeid.replace('::', '_')}",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                raise Exception(f'Не удалось выполнить скриншот: {str(e)}')
