from pages.main_page import MainPage
from pages.company_card_page import CompanyCardPage
from pages.base_page import BasePage
from pages.modules_page import ModulesPage
from pages.rosregistry_page import RegistryPage


class PageFactory:
    def __init__(self, driver):
        self.driver = driver
        self._cache = {}

    @property
    def base(self) -> BasePage:
        if 'base' not in self._cache:
            self._cache['base'] = BasePage(self.driver)
        return self._cache['base']

    @property
    def main(self) -> MainPage:
        if 'main' not in self._cache:
            self._cache['main'] = MainPage(self.driver)
        return self._cache['main']

    @property
    def company(self) -> CompanyCardPage:
        if 'company' not in self._cache:
            self._cache['company'] = CompanyCardPage(self.driver)
        return self._cache['company']

    @property
    def modules(self) -> ModulesPage:
        if 'modules' not in self._cache:
            self._cache['modules'] = ModulesPage(self.driver)
        return self._cache['modules']

    @property
    def registry(self) -> RegistryPage:
        if 'registry' not in self._cache:
            self._cache['registry'] = RegistryPage(self.driver)
        return self._cache['registry']
