class LoginAndSecurityPage():

    def __init__(self, logger, webdriver, base_page):
        self.saveto = logger
        self.bp = base_page
        self.driver = webdriver

    # Locators
    edit_name_button_xpath = ".//*[@id='auth-cnep-edit-name-button']"

    # Constants
    duplicate_username_error_message = 'An account already exists with this username.'
    duplicate_email_message = "An account already exists with this email."
    EMPTY_EMAIL_VALIDATION_MSG = "Enter your email or mobile phone number"

    # Functions
    def click_on_edit_button(self):
        self.bp.element_click_by_xpath(self.edit_name_button_xpath)
