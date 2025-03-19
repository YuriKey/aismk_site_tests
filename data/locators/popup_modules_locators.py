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

    CLOSE_POPUP_BUTTON = (By.XPATH, '//*[@class="e-font-icon-svg e-eicon-close eicon-close"]')

    POPUP_AREA = (By.XPATH, '//*[@data-elementor-type="popup"]')

    HEADER_LOCATOR = (By.XPATH, '//h1[@class="elementor-heading-title elementor-size-default"]')
