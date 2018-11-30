from screens.first_screen import FirstScreen
from screens.sign_in_cell_phone_screen import SignInCellPhoneScreen
from screens.country_code_screen import CountryCodeScreen
import time


class SignInControls(object):
    def __init__(self, driver, logger, email, platform, phone_number, password, country_name="United States"):
        """
        Wraps the login steps: select country code, input phone number and password, and click Sign In.

        :param driver: The web driver to locate the element
        :param logger: The logger to log to
        :param phone_number: The sign in phone number
        :param password: The sign in passoword
        :param platform: The platform either andriod or ios
        :param country_code: The country name shown on our application
        """
        self.country_name = country_name
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.driver = driver
        self.platform = platform
        self.logger = logger
        self.first_screen = FirstScreen(self.logger, self.driver, self.platform)
        self.sign_in_cell_screen = SignInCellPhoneScreen(self.logger, self.driver, self.platform)
        self.country_code_screen = CountryCodeScreen(self.logger, self.driver, self.platform)

    def phone_number_sign_in(self):
        """
        :return:
        """
        self.first_screen.getElement(self.first_screen.ElementIds.SignIn, self.driver).click()
        self.sign_in_cell_screen.getElement(self.sign_in_cell_screen.ElementIds.countryCode, self.driver).click()
        self.country_code_screen.getElement(self.country_code_screen.ElementIds[self.country_code_screen.ElementIds(self.country_name).name], self.driver).click()
        self.sign_in_cell_screen.getElement(self.sign_in_cell_screen.ElementIds.yourCellPhoneNumber, self.driver).set_value(self.phone_number)
        self.sign_in_cell_screen.getElement(self.sign_in_cell_screen.ElementIds.password,self.driver).set_value(self.password)
        self.sign_in_cell_screen.getElement(self.sign_in_cell_screen.ElementIds.signIn, self.driver).click()

    def email_sign_in(self):
        """
        :return:
        """
        # self.driver.find_element_by_accessibility_id("Sign In").click()
        self.first_screen.getElement(FirstScreen.ElementIds.SignIn, self.driver).click()
        self.sign_in_cell_screen.getElement(self.sign_in_cell_screen.ElementIds.signInWithEmail, self.driver).click()
        self.sign_in_cell_screen.getElement(self.sign_in_cell_screen.ElementIds.password, self.driver).set_value(self.email)
        self.sign_in_cell_screen.getElement(self.sign_in_cell_screen.ElementIds.signIn, self.driver).click()

    def get_phone_and_password_not_match_error_text(self):
        """
        :return:
        """
        return self.sign_in_cell_screen.getElement(self.sign_in_cell_screen.ElementIds.phoneAndPasswordNotMatch, self.driver).text

    def get_password_length_error_text(self):
        print (self.sign_in_cell_screen.getElement(self.sign_in_cell_screen.ElementIds.passwordLengthError, self.driver).text)
        return self.sign_in_cell_screen.getElement(self.sign_in_cell_screen.ElementIds.passwordLengthError, self.driver).text

    def get_phone_length_error_text(self):
        return self.sign_in_cell_screen.getElement(self.sign_in_cell_screen.ElementIds.phoneLengthError, self.driver).text

    def get_heading_text(self):
        return self.sign_in_cell_screen.getElement(self.sign_in_cell_screen.ElementIds.heading_text, self.driver).text

    def alert_switch(self):
        self.driver.switch_to_alert()

    def get_email_invalid_error_text(self):
        return self.sign_in_cell_screen.getElement(self.sign_in_cell_screen.ElementIds.email_error, self.driver).text

    def forget_password_phone(self):
        """
        :return:
        """
        self.first_screen.getElement(FirstScreen.ElementIds.SignIn, self.driver).click()
        self.sign_in_cell_screen.getElement(self.sign_in_cell_screen.ElementIds.forgotPassword, self.driver).click()
        self.sign_in_cell_screen.getElement(self.sign_in_cell_screen.ElementIds.your_cell_phone_number_forget_password,
                                            self.driver).set_value(self.phone_number)
        self.sign_in_cell_screen.getElement(self.sign_in_cell_screen.ElementIds.reset_password, self.driver).click()
        time.sleep(15)

    def forget_password_email(self):
        """
        :return:
        """
        self.first_screen.getElement(FirstScreen.ElementIds.SignIn, self.driver).click()
        self.sign_in_cell_screen.getElement(self.sign_in_cell_screen.ElementIds.forgotPassword, self.driver).click()
        self.sign_in_cell_screen.getElement(self.sign_in_cell_screen.ElementIds.your_email,
                                            self.driver).send_keys("abc")
        self.sign_in_cell_screen.getElement(self.sign_in_cell_screen.ElementIds.reset_password, self.driver).click()