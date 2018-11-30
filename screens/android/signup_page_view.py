from locators.locators import AndroidCreateProfile as Xpath
from screens.screen_base import Screen


class SignUpPageView(Screen):

    def find_country_code(self):
        return self.driver.find_element_by_xpath(Xpath.country_code_xpath)

    def find_field_password(self):
        return self.driver.find_element_by_xpath(Xpath.password_xpath)

    def find_field_cell_phone_number(self):
        return self.driver.find_element_by_xpath(Xpath.cell_phone_number_xpath)

    def find_field_email_address(self):
        return self.driver.find_element_by_xpath(Xpath.email_address_xpath)

    def find_checkbox_agree(self):
        return self.driver.find_element_by_xpath(Xpath.agree_to_xpath)

    def find_signup_button(self):
        return self.driver.find_element_by_xpath(Xpath.sign_up_xpath)

    def find_accept_button(self):
        return self.driver.find_element_by_xpath(Xpath.accept_xpath)

    def find_decline_button(self):
        return self.driver.find_element_by_xpath(Xpath.decline_xpath)

    def find_pin(self, index):
        if index == 0:
            return self.driver.find_element_by_xpath(Xpath.pin_0_xpath)
        elif index == 1:
            return self.driver.find_element_by_xpath(Xpath.pin_1_xpath)
        elif index == 2:
            return self.driver.find_element_by_xpath(Xpath.pin_2_xpath)
        elif index == 3:
            return self.driver.find_element_by_xpath(Xpath.pin_3_xpath)

    def find_enter_code_manually(self):
        return self.driver.find_element_by_xpath(Xpath.imei)

    def find_code(self, index):
        return self.driver.find_element_by_xpath(Xpath.code_xpath % index)

    def find_imei_continue(self):
        return self.driver.find_element_by_xpath(Xpath.imei_continue_xpath)

    def find_insert_sim_card_continue(self):
        return self.driver.find_element_by_xpath(Xpath.sim_card_continue_xpath)

    def find_install_device_continue(self):
        return self.driver.find_element_by_xpath(Xpath.install_device_continue_xpath)

    def find_cancel_connecting_device(self):
        return self.driver.find_element_by_xpath(Xpath.cancel_connecting_device_xpath)

    def find_confirm_discard_device_activation_button(self):
        return self.driver.find_element_by_xpath(Xpath.confirm_discard_device_activation_xpath)