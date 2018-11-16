from web_helper.credential_helper import CredentialHelper


class SignInPage():

    def __init__(self, logger, webdriver, base_page):
        self.saveto = logger
        self.bp = base_page
        self.driver = webdriver

    # Locators
    email_text_field_xpath = "//input[@name='email']"
    password_text_field_xpath = "//input[@name='password']"
    continue_button_class = "a-button-input"
    empty_email_validation_msg_xpath = ".//*[@id='auth-email-missing-alert']/div/div"
    create_acc_button_xpath = "//input[@type='submit']"
    create_acc_button_id = "createAccountSubmit"
    your_name_field_id = "ap_customer_name"
    email_field_id = "ap_email"
    password_field_id = "ap_password"
    re_enter_password_field_id = "ap_password_check"

    # Constants
    duplicate_username_error_message = 'An account already exists with this username.'
    duplicate_email_message = "An account already exists with this email."
    EMPTY_EMAIL_VALIDATION_MSG = "Enter your email or mobile phone number"
    EMPTY_PWD_VALIDATION_MSG = "Enter your password"

    # Functions
    def create_a_new_account(self):
        self.bp.enter_value_in_text_field_by_id(self.your_name_field_id, CredentialHelper.username)
        self.bp.enter_value_in_text_field_by_id(self.email_field_id, CredentialHelper.valid_email)
        self.bp.enter_value_in_text_field_by_id(self.password_field_id, CredentialHelper.valid_password)
        self.bp.enter_value_in_text_field_by_id(self.re_enter_password_field_id, CredentialHelper.valid_password)
        self.bp.element_click_by_xpath(self.create_acc_button_xpath)

    def login_with_email_password(self, email, password):
        self.bp.enter_value_in_text_field_by_id(self.email_field_id, email)
        self.bp.enter_value_in_text_field_by_id(self.password_field_id, password)
        self.bp.element_click_by_xpath(self.create_acc_button_xpath)

    def login_with_empty_email_id(self, email):
        self.bp.enter_value_in_text_field_by_xpath(self.email_text_field_xpath, email)
        self.bp.element_click_by_class(self.continue_button_class)
