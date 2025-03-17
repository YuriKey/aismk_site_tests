from selenium.webdriver.common.by import By


class CardPageLocators:
    COMPANY_CARD_BUTTON = (By.XPATH, '//a[@class="elementor-item"][not(@tabindex="-1")][contains(text(), "Карточка '
                                     'предприятия")]')
    COMPANY_CARD_BUTTON_FOOTER = (By.XPATH, '//*[@class="elementor-icon-list-text"][contains(text(), "Карточка предприятия")]')
