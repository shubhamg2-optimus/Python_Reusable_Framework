class YourAccountPage():

    def __init__(self, logger, webdriver, base_page):
        self.saveto = logger
        self.bp = base_page
        self.driver = webdriver

    # Locators
    login_and_security_card_xpath = "//h2[contains(text(),'Login & security')]"

    # Functions
    def navigate_to_login_and_security_page(self):
        self.bp.element_click_by_xpath(self.login_and_security_card_xpath)