from selenium.webdriver.common.by import By


class RegistryPageLocators:
    REGISTRY_BUTTON = (By.XPATH, '//*[@class="elementor-element elementor-element-56d6e93 elementor-align-left '
                                 'elementor-widget elementor-widget-button"]')
    OWNER_TITLE = (By.XPATH, '//*[@href="/promo/owner/1284851/1119621/"]')
    OWNER_SHORT_TITLE = (By.XPATH, '//div[@class="col-md-4 mb-4"][.//label[contains(text(), "Сокращенное")]]//div['
                                   '@class="fs-5"]')
    HEADER_TITLE = (By.XPATH, '//h1')
    SOFT_FULL_TITLE = (By.XPATH, '//div[@class="mb-4"][.//label[contains(text(), "наименования")]]//div['
                                 '@class="form-area"]')
