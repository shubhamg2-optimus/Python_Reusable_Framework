from screens.android.signin_email_page_view import SignInEmailPageView

class SignInEmailPage():

    def __init__(self, driver):
        self.page = SignInEmailPageView(driver)

    def type_your_email_address(self, your_email_address):
        self.page.find_field_your_email_address().set_value(your_email_address)

    def type_your_password(self, password):
        self.page.find_field_password().set_value(password)

    def click_sign_in(self):
        self.page.find_button_sign_in().click()