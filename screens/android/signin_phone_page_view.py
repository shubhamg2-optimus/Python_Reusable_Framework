from locators.locators import AndroidSignInPhoneNumber as Locator
from locators.locators import AndroidSignInPhoneNumber as Xpath
from screens.screen_base import Screen


class SignInPhoneNumberPageView(Screen):

    def find_country_code(self):
        return self.driver.find_element_by_id(Locator.country_code_id)

    def find_field_password(self):
        return self.driver.find_element_by_xpath(Xpath.password_xpath)

    def find_field_cell_phone_number(self):
        return self.driver.find_element_by_id(Locator.your_cell_phone_number_id)

    def find_link_forgot_password(self):
        return self.driver.find_element_by_id(Locator.fogot_password_id)

    def find_button_sign_in(self):
        return self.driver.find_element_by_id(Locator.sign_in_id)

    def find_link_sign_in_with_email(self):
        return self.driver.find_element_by_id(Locator.sign_in_with_email_id)

    def find_phone_error_text(self):
        return self.driver.find_element_by_id(Locator.error_text_id)

    def find_password_error_text(self):
        return self.driver.find_element_by_xpath(Xpath.password_error_text_xpath)