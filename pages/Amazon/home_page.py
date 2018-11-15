import time

class HomePage():

    def __init__(self, logger, webdriver, base_page):
        self.saveto = logger
        self.bp = base_page
        self.driver = webdriver

    # Locators
    Sign_in_dropdown_xpath = "//div[@id='nav-tools']/a"


    # Constants


    # Functions
    def navigate_to_sign_in_page(self):
        self.bp.element_click_by_xpath(self.Sign_in_dropdown_xpath)
        time.sleep(5)


