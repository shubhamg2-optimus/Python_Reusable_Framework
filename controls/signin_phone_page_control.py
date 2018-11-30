from screens.android.signin_phone_page_view import SignInPhoneNumberPageView


class SignInPhoneNumberPage():

    def __init__(self, driver):
        self.page = SignInPhoneNumberPageView(driver)

    def load_country_code_page(self):
        return self.page.find_country_code().click()

    def type_phone_number(self, phone_number):
        self.page.find_field_cell_phone_number().set_value(phone_number)

    def type_password(self, password):
        self.page.find_field_password().set_value(password)

    def click_forgot_password(self):
        self.page.find_link_forgot_password()

    def click_sign_in(self):
        self.page.find_button_sign_in().click()

    def click_sign_in_with_email(self):
        self.page.find_link_sign_in_with_email().click()

    def look_at_country_code(self):
        return self.page.find_country_code().text

    def get_phone_error_message(self):
        return self.page.find_phone_error_text().text

    def get_password_error_message(self):
        return self.page.find_password_error_text().text