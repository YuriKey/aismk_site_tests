from selenium.webdriver.common.by import By


class MainPageLocators:
    REGISTRY_BUTTON = (By.XPATH, '//*[@class="elementor-element elementor-element-56d6e93 elementor-align-left '
                                 'elementor-widget elementor-widget-button"]')
    OFFER_BUTTON = (By.XPATH, '//*[@class="elementor-button-link elementor-button elementor-size-md"]')
    PHONE_HEADER = (By.XPATH, '//*[@class="elementor-heading-title elementor-size-default"][contains(text(),'
                              '"+7 (8422) 26-09-27")]')
    CONTACTS_FOOTER = (By.XPATH, '//*[@class="elementor-heading-title elementor-size-default"][contains(text(),'
                                 '"Радищева")]')
    EMAIL_FOOTER = (By.XPATH, '//*[@class="elementor-heading-title elementor-size-default"][contains(text(),'
                              '"support@aismk.ru")]')
