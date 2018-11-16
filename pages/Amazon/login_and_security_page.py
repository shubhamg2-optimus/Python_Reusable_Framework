class LoginAndSecurityPage():

    def __init__(self, logger, webdriver, base_page):
        self.saveto = logger
        self.bp = base_page
        self.driver = webdriver

    # Locators
    edit_name_button_xpath = ".//*[@id='auth-cnep-edit-name-button']"
    new_name_text_field_xpath = "//input[@id='ap_customer_name']"
    save_changes_button_xpath = "//span[@id='a-autoid-0']"
    success_msg_xpath = "//span[contains(text(),'You have successfully modified your account!')]"

    # Constants
    EMPTY_EMAIL_VALIDATION_MSG = "Enter your email or mobile phone number"
    USERNAME_UPDATED_SUCCESS_MSG = "You have successfully modified your account!"

    # Functions
    def update_user_name(self,username):
        self.bp.element_click_by_xpath(self.edit_name_button_xpath)
        self.bp.enter_value_in_text_field_by_xpath(self.new_name_text_field_xpath, username)
        self.bp.element_click_by_xpath(self.save_changes_button_xpath)



