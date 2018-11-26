import time


class HomePage():

    def __init__(self, logger, webdriver, base_page):
        self.saveto = logger
        self.bp = base_page
        self.driver = webdriver

    # Locators
    sign_in_dropdown_xpath = "//div[@id='nav-tools']/a[2]"
    username_xpath = "//*[@class='nav-a nav-a-2 nav-truncate']//span[@class='nav-line-1']"
    sign_in_button_xpath = "//a[@class='nav-action-button']"

    # Functions
    def navigate_to_sign_in_page(self):
        self.bp.perform_hover_by_xpath(self.sign_in_dropdown_xpath)
        self.bp.element_click_by_xpath(self.sign_in_button_xpath)

    def navigate_to_your_orders_page(self):
        self.bp.perform_hover_by_xpath(self.sign_in_dropdown_xpath)
        self.bp.element_click_by_link_text("Your Orders")

    def navigate_to_sign_up_page(self):
        self.bp.perform_hover_by_xpath(self.sign_in_dropdown_xpath)
        self.bp.element_click_by_link_text("Start here.")
        time.sleep(10)

    def get_username(self):
        return self.driver.find_element_by_xpath(self.username_xpath).text.split(" ")[1]

    def navigate_to_your_account_page(self):
        self.bp.perform_hover_by_xpath(self.sign_in_dropdown_xpath)
        self.bp.element_click_by_link_text("Your Account")

    def log_out_account(self):
        self.bp.perform_hover_by_xpath(self.sign_in_dropdown_xpath)
        self.bp.element_click_by_link_text("Sign Out")
