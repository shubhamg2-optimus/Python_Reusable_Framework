from controls_old.preface_page_control import PrefacePage
from controls_old.signup_page_control import SignUpPage

import utils.general_utility as utils
from base_test import BastTest
from controls.country_code_page import CountryCodePage


class SignUpTest(BastTest):
    def test_sign_up_succeeds(self):
        promo_page = PrefacePage(self.driver)
        promo_page.click_signUp()

        signup_page = SignUpPage(self.driver)
        signup_page.load_country_code_page()

        country_code_page = CountryCodePage(self.driver)
        country_code_page.select_code(code="united_states")

        phone = "000999%s" % utils.num_string_generator(size=4)
        email = utils.email_generator(name=(utils.firstname()+utils.lastname()))
        signup_page.type_phone_number(phone)
        signup_page.type_email_address(email)
        signup_page.type_password("Test123")
        self.saveto.logger.info("email: %s, phone_number: %s, password: %s" % (phone, email, "Test123"))

        signup_page.click_agree_checkbox()
        signup_page.scroll_down_to_enable_accept_button_for_agreement()
        signup_page.click_accept_button()
        signup_page.click_signup_button()

        signup_page.type_pin_number(0, "1")
        signup_page.type_pin_number(1, "1")
        signup_page.type_pin_number(2, "3")
        signup_page.type_pin_number(3, "7")

        signup_page.click_enter_code_manually()

        imei = "999" + utils.num_string_generator(size=12)
        self.saveto.logger.info("IMEI barcode(internal use only): %s" % imei)

        for i in range(1, 16):
            signup_page.type_imei_number(i, imei[i-1])

        signup_page.click_continue_imei()
        signup_page.click_continue_sim_card()
        signup_page.click_continue_install_device()
        signup_page.click_cancel_connecting_to_your_car()