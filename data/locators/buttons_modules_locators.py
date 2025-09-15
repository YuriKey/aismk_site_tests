from selenium.webdriver.common.by import By


class PopupModulesLocators:
    POPUP_BUTTON = (By.XPATH, '//*[@data-id="446e1fbd"]')
    POPUP_UR = (By.XPATH, '//*[@href="/ur/"]')
    POPUP_UM = (By.XPATH, '//*[@href="/um/"]')
    POPUP_SK = (By.XPATH, '//*[@href="/sk/"]')
    POPUP_MP = (By.XPATH, '//*[@href="/mp/"]')
    POPUP_IS = (By.XPATH, '//*[@href="/is/"]')
    POPUP_AR = (By.XPATH, '//*[@href="/ar/"]')
    POPUP_VK = (By.XPATH, '//*[@href="/vk/"]')
    POPUP_AU = (By.XPATH, '//*[@href="/au/"]')
    POPUP_AKP = (By.XPATH, '//*[@href="/akp/"]')
    POPUP_US = (By.XPATH, '//*[@href="/us/"]')

    CLOSE_POPUP_BUTTON = (By.XPATH, '//*[@class="e-font-icon-svg e-eicon-close eicon-close"]')

    POPUP_AREA = (By.XPATH, '//*[@data-elementor-type="popup"]')

    HEADER_TEXT = (By.XPATH, '//h1[@class="elementor-heading-title elementor-size-default"]')

    OFFER_BUTTON = (By.XPATH, '//*[@class="elementor-button-text"]')


class FooterModulesLocators(PopupModulesLocators):
    FOOTER_UR = (By.XPATH, '//*[@href="https://aismk.ru/ur/"][ancestor::*[@id="menu-1-0512d26"]]')
    FOOTER_UM = (By.XPATH, '//*[@href="https://aismk.ru/um/"][ancestor::*[@id="menu-1-0512d26"]]')
    FOOTER_SK = (By.XPATH, '//*[@href="https://aismk.ru/sk/"][ancestor::*[@id="menu-1-0512d26"]]')
    FOOTER_MP = (By.XPATH, '//*[@href="https://aismk.ru/mp/"][ancestor::*[@id="menu-1-0512d26"]]')
    FOOTER_IS = (By.XPATH, '//*[@href="https://aismk.ru/is/"][ancestor::*[@id="menu-1-0512d26"]]')
    FOOTER_AR = (By.XPATH, '//*[@href="https://aismk.ru/ar/"][ancestor::*[@id="menu-1-0512d26"]]')
    FOOTER_VK = (By.XPATH, '//*[@href="https://aismk.ru/vk/"][ancestor::*[@id="menu-1-0512d26"]]')
    FOOTER_AU = (By.XPATH, '//*[@href="https://aismk.ru/au/"][ancestor::*[@id="menu-1-0512d26"]]')
    FOOTER_AKP = (By.XPATH, '//*[@href="https://aismk.ru/akp/"][ancestor::*[@id="menu-1-0512d26"]]')
    FOOTER_US = (By.XPATH, '//*[@href="https://aismk.ru/us/"][ancestor::*[@id="menu-1-0512d26"]]')

