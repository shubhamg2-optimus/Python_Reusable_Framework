from locators.locators import AndroidSignInEmail as Locator
from locators.locators import AndroidSignInEmail as Xpath
from screens.screen_base import Screen


class SignInEmailPageView(Screen):

    def find_field_your_email_address(self):
        return self.driver.find_element_by_id(Locator.your_email_address_id)

    def find_field_password(self):
        return self.driver.find_element_by_xpath(Xpath.password_xpath)

    def find_link_forgot_password(self):
        return self.driver.find_element_by_id(Locator.fogot_password)

    def find_button_sign_in(self):
        return self.driver.find_element_by_id(Locator.sign_in_id)

    def find_link_sign_in_with_phone_number(self):
        return self.driver.find_element_by_id(Locator.sign_in_with_phone_number_id)