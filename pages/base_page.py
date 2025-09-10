import time

import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 5)

    def open(self, url: str) -> None:
        with allure.step('Открытие страницы по URL'):
            try:
                self.browser.get(url)
            except Exception as e:
                raise Exception(f'Не удалось открыть страницу по URL {url}: {e}')

    def find_element(self, locator: tuple[str, str]) -> WebElement:
        with allure.step(f'Поиск элемента по локатору {locator}'):
            try:
                return self.wait.until(EC.visibility_of_element_located(locator))
            except Exception as e:
                raise Exception(f'Не удалось найти элемент по локатору {locator}: {e}')

    def click_element(self, locator: tuple[str, str]) -> None:
        with allure.step(f'Клик по элементу с локатором: {locator}'):
            try:
                self.wait.until(
                    EC.element_to_be_clickable(locator),
                    message=f'Не удалось найти кликабельный элемент с локатором {locator}'
                ).click()
            except Exception as e:
                raise Exception(f'Не удалось кликнуть по элементу с локатором {locator}: {e}')

    def click_element_by_js(self, element: object) -> None:
        with allure.step('Клик по элементу с помощью JS'):
            try:
                self.browser.execute_script("""
                    var elem = arguments[0];
                    var event = new MouseEvent('click', {
                        bubbles: true,
                        cancelable: true,
                        view: window
                    });
                    elem.dispatchEvent(event);
                """, element)
            except Exception as e:
                raise Exception(f'Не удалось выполнить JS-клик: {str(e)}')

    def fill_field(self, locator: tuple[str, str], text: str) -> None:
        with allure.step('Заполнение поля'):
            try:
                self.find_element(locator).send_keys(text)
            except Exception as e:
                raise Exception(f'Не удалось заполнить поле: {str(e)}')

    def element_is_displayed(self, locator: tuple[str, str]) -> bool:
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except:
            return False

    def get_current_url(self) -> str:
        with allure.step('Получение URL текущей страницы'):
            try:
                return self.browser.current_url
            except Exception as e:
                raise Exception(f'Не удалось получить URL текущей страницы: {str(e)}')

    def get_title(self) -> str:
        with allure.step('Получение заголовка страницы'):
            try:
                return self.browser.title
            except Exception as e:
                raise Exception(f'Не удалось получить заголовок страницы: {str(e)}')

    def refresh_page(self) -> None:
        with allure.step('Обновление страницы'):
            self.browser.refresh()

    def scroll_to_element(self, locator: tuple[str, str]) -> None:
        with allure.step('Скроллинг до элемента'):
            try:
                element = self.find_element(locator)
                self.browser.execute_script('arguments[0].scrollIntoView({behavior: "auto", block: "center"});',
                                            element)

            except Exception as e:
                raise Exception(f'Ошибка при скроллинге до элемента: {str(e)}')

    def switch_to_alert(self):
        with allure.step('Переключение на алерт'):
            try:
                WebDriverWait(self.browser, 5).until(EC.alert_is_present())
                alert = self.browser.switch_to.alert
                return alert
            except Exception as e:
                raise Exception(f'Не удалось переключиться на алерт: {e}')

    def accept_alert(self):
        with allure.step('Подтверждение алерта'):
            try:
                self.wait.until(EC.alert_is_present())
                alert = self.browser.switch_to.alert
                alert.accept()
            except Exception as e:
                raise Exception(f'Не удалось подтвердить алерт: {e}')

    @staticmethod
    def get_text(element: object) -> str:
        try:
            return element.text
        except Exception as e:
            raise Exception(f'Не удалось получить текст из элемента: {e}')

    @staticmethod
    def await_for_js_reaction() -> None:
        time.sleep(2)
