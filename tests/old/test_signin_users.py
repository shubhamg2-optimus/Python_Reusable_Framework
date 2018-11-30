import unittest

from controls_old.account_page_control import AccountPage
from controls_old.country_code_page import CountryCodePage
from controls_old.home_page_control import HomePage
from controls_old.preface_page_control import PrefacePage
from controls_old.signin_email_page_control import SignInEmailPage
from controls_old.signin_phone_page_control import SignInPhoneNumberPage

from base_test import BastTest
from controls.navigation_page_control import NavigationPage
from screens import android as E


class SignInTest(BastTest):

    def test_valid_signin_with_correct_phonenumber_and_password(self):
        promo_page = PrefacePage(self.driver)
        promo_page.click_signIn()

        signin_page = SignInPhoneNumberPage(self.driver)
        signin_page.load_country_code_page()
        code_page = CountryCodePage(self.driver)

        code_page.select_code(code="united_states")

        signin_page.type_phone_number(self.phonenumber)
        signin_page.type_password(self.password)
        signin_page.click_sign_in()
        self.driver.implicitly_wait(30)

        home_page = HomePage(self.driver)
        home_page.load_navigation_page()

        navigation_page = NavigationPage(self.driver)
        navigation_page.load_account_page()

        account_page = AccountPage(self.driver)
        account_page.load_log_out_container()
        account_page.confirm_log_out()

    def test_valid_signin_with_correct_email_and_password(self):
        promo_page = PrefacePage(self.driver)
        promo_page.click_signIn()

        signin_page = SignInPhoneNumberPage(self.driver)
        signin_page.click_sign_in_with_email()

        signin_email_page = SignInEmailPage(self.driver)
        signin_email_page.type_your_email_address(self.email)
        signin_email_page.type_your_password(self.password)
        signin_email_page.click_sign_in()
        self.driver.implicitly_wait(30)

        home_page = HomePage(self.driver)
        home_page.load_navigation_page()

        navigation_page = NavigationPage(self.driver)
        navigation_page.load_account_page()

        account_page = AccountPage(self.driver)
        account_page.load_log_out_container()
        account_page.confirm_log_out()

    def test_invalid_signin_with_wrong_password(self):
        promo_page = PrefacePage(self.driver)
        promo_page.click_signIn()

        signin_page = SignInPhoneNumberPage(self.driver)
        signin_page.load_country_code_page()
        code_page = CountryCodePage(self.driver)
        code_page.select_code(code="united_states")
        signin_page.type_phone_number(self.phonenumber)
        signin_page.type_password("wrong password")
        signin_page.click_sign_in()
        self.driver.implicitly_wait(30)

        self.assertTrue(signin_page.get_phone_error_message() == E.SIGN_IN_ERROR)

    def test_invalid_sigin_with_invalid_phonenumber(self):
        promo_page = PrefacePage(self.driver)
        promo_page.click_signIn()

        signin_page = SignInPhoneNumberPage(self.driver)
        signin_page.type_phone_number(self.phonenumber)
        signin_page.type_password(self.password)
        signin_page.click_sign_in()

        self.assertTrue(signin_page.get_phone_error_message() == E.SIGN_IN_ERROR)

    def test_invalid_signin_with_phonenumber_under_seven_digits(self):
        promo_page = PrefacePage(self.driver)
        promo_page.click_signIn()

        signin_page = SignInPhoneNumberPage(self.driver)
        signin_page.type_phone_number("666666")
        signin_page.type_password("55555")
        signin_page.click_sign_in()
        self.assertTrue(signin_page.get_phone_error_message() == E.PHONE_NUMBER_LENGTH_ERROR)
        self.assertTrue(signin_page.get_password_error_message() == E.PASSWORD_LENGTH_ERROR)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SignInTest)
    unittest.TextTestRunner(verbosity=2).run(suite)