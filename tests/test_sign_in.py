import unittest

from tests.base_test import BaseTest
from controls.login_controls import SignInControls
from screens.country_code_screen import CountryCodeScreen
from screens.modes import PlatformSupported
from screens.elements.errors import SignInErrors
from utils.decorators import test_case
import time

class SignInTest(BaseTest):

    @test_case(id="8164")
    def test_001_valid_signin_with_correct_cell_and_password(self):
        valid = SignInControls(self.driver, self.logger, self.email,self.platform, self.phonenumber, self.password,
                               country_name="United States")

        valid.phone_number_sign_in()
        # TODO: Verification of Successful Sign In
        time.sleep(5)

    @test_case(id="8168")
    def test_002_invalid_signin_with_not_matched_cell_and_password(self):
        invalid = SignInControls(self.driver, self.logger, self.email, self.platform, self.phonenumber, "password not match",
                                 country_name=CountryCodeScreen.ElementIds.UnitedStates)
        invalid.phone_number_sign_in()
        self.driver.implicitly_wait(30)
        self.assertTrue(invalid.get_phone_and_password_not_match_error_text() == SignInErrors.SHARED_CELL_AND_PWD_DO_NOT_MATCH)
        time.sleep(5)

    @test_case(id="10121")
    def test_003_invalid_signin_with_not_short_phonenumber(self):
        invalid = SignInControls(self.driver, self.logger, self.email, self.platform, "510", self.password,
                                 country_name=CountryCodeScreen.ElementIds.UnitedStates)

        invalid.phone_number_sign_in()
        self.driver.implicitly_wait(30)
        if self.platform == PlatformSupported.ANDROID:
            self.assertTrue(invalid.get_phone_length_error_text() == SignInErrors.ANDROID_AT_LEAST_SEVEN_DIGITS,
                            "Received: %s" % invalid.get_phone_length_error_text())
        elif self.platform == PlatformSupported.IOS:
            self.assertTrue(invalid.get_phone_length_error_text() == SignInErrors.IOS_ENTER_A_VALID_CELL_PHONE)

    @test_case(id="C199853")
    def test_004_invalid_signin_with_not_short_password(self):
        invalid = SignInControls(self.driver, self.logger, self.email, self.platform, self.phonenumber, "123",
                                 country_name=CountryCodeScreen.ElementIds.UnitedStates)
        invalid.phone_number_sign_in()
        self.driver.implicitly_wait(30)

        self.assertTrue(invalid.get_password_length_error_text() == SignInErrors.SHARED_BETWEEN_SIX_AND_THIRTYTWO)

    @test_case(id="8071")
    def test_005_invalid_phone_forget_password(self):
        invalid = SignInControls(self.driver, self.logger, self.email, self.platform, self.password, self.password,
                                 country_name=CountryCodeScreen.ElementIds.UnitedStates)

        invalid.forget_password_phone()

        if self.platform == PlatformSupported.ANDROID:
            self.assertTrue(invalid.get_phone_length_error_text() == SignInErrors.ANDROID_NO_ACCOUNT_FOUND,
                            "Received: %s" % invalid.get_phone_length_error_text())
        elif self.platform == PlatformSupported.IOS:
            self.assertTrue(invalid.get_phone_length_error_text() == SignInErrors.IOS_ENTER_A_VALID_CELL_PHONE)


    @test_case(id="8071")
    def test_006_invalid_email_forget_password(self):
        invalid = SignInControls(self.driver, self.logger, "abc", self.platform, self.password, self.password,
                                 country_name=CountryCodeScreen.ElementIds.UnitedStates)
        invalid.forget_password_email()

        if self.platform == PlatformSupported.ANDROID:
            self.assertTrue(invalid.get_phone_length_error_text() == SignInErrors.ANDROID_ENTER_INVALID_EMAIl,
                            "Received: %s" % invalid.get_phone_length_error_text())
        elif self.platform == PlatformSupported.IOS:
                self.assertTrue(invalid.get_email_invalid_error_text() == SignInErrors.IOS_ENTER_INVALID_EMAIl)

    @test_case(id="8070")
    def test_006_correct_phone_forget_password(self):
        valid = SignInControls(self.driver, self.logger, self.email, self.platform, self.phonenumber, self.password,
                               country_name=CountryCodeScreen.ElementIds.UnitedStates)
        valid.forget_password_phone()

        if self.platform == PlatformSupported.ANDROID:
            self.assertTrue(valid.get_heading_text() == SignInErrors.RESET_PASSWORD,
                            "Received: %s" % valid.get_heading_text())
        elif self.platform == PlatformSupported.IOS:
            time.sleep(5)
            # TODO: Verification of  Message

    @test_case(id="8070")
    def test_006_correct_email_forget_password(self):
        valid = SignInControls(self.driver, self.logger, self.email, self.platform, self.phonenumber, self.password,
                               country_name=CountryCodeScreen.ElementIds.UnitedStates)

        valid.forget_password_email()
        valid.alert_switch()

        if self.platform == PlatformSupported.ANDROID:
            self.assertTrue(valid.get_heading_text() == SignInErrors.RESET_PASSWORD,
                            "Received: %s" % valid.get_heading_text())
        elif self.platform == PlatformSupported.IOS:
            time.sleep(5)
            # TODO: Verification of  Message

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SignInTest)
    unittest.TextTestRunner(verbosity=2).run(suite)