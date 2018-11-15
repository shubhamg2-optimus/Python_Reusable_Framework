import time

class HomePage():

    def __init__(self, logger, webdriver, base_page):
        self.saveto = logger
        self.bp = base_page
        self.driver = webdriver

    # Locators
    Sign_in_dropdown_class = "nav-a nav-a-2-active"

    # Constants


    # Functions
    def navigate_to_sign_in_page(self):
        self.bp.element_click_by_class(self.Sign_in_dropdown_class)
        time.sleep(20)


