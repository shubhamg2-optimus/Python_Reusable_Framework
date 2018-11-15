class SignInPage():

    def __init__(self, logger, webdriver, base_page):
        self.saveto = logger
        self.bp = base_page
        self.driver = webdriver

    # Locators
    page_title_xpath = "//p-header"
    delete_icon_xpath = "//a[@class='icon trash']"

    # Constants
    duplicate_username_error_message = 'An account already exists with this username.'
    duplicate_email_message = "An account already exists with this email."

    # Functions
    def login_with_email_password(self, email, password):
        print("success")