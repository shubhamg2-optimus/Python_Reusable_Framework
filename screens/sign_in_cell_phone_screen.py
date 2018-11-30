from screens.modes import PlatformSupported
from screens.elements.holder import Holder
from screens.screen_base import ScreenBase
from locators.locators import AndroidSignInPhoneNumber, AndroidSignInPhoneNumber
import enum

class SignInCellPhoneScreen(ScreenBase):
    @enum.unique
    class ElementIds(enum.Enum):
        # Common elements shared by both platforms
        countryCode = "country code"
        yourCellPhoneNumber = "Your cell phone number"
        password = "Password"
        forgotPassword = "Forgot Password"
        signIn = "sign In"
        signInWithEmail = "Sign In with Email"
        phoneAndPasswordNotMatch = "Not Match Error"
        phoneLengthError = "Phone Length Error"
        passwordLengthError = "Password Length Error"
        your_cell_phone_number_forget_password = "Your cell phone number Forget password"
        reset_password = "Reset Password"
        your_email="Your email"
        email_error = "Enter valid email id"
        heading_text = "Reset Password heading"


    def __init__(self, logger, driver, platform):
        """
        The first screen will be displayed after the application launches successfully.

        :param logger: The logger to log to
        :param driver: The web driver
        :param platform: The platform that automation will run on
        """

        super().__init__(logger, platform)

        if platform == PlatformSupported.ANDROID:
            self.elements = {
                self.ElementIds.countryCode: Holder(driver.find_element_by_id, AndroidSignInPhoneNumber.country_code_id),
                self.ElementIds.yourCellPhoneNumber: Holder(driver.find_element_by_id, AndroidSignInPhoneNumber.your_cell_phone_number_id),
                self.ElementIds.password: Holder(driver.find_element_by_xpath, AndroidSignInPhoneNumber.password_xpath),
                self.ElementIds.signIn: Holder(driver.find_element_by_id, AndroidSignInPhoneNumber.sign_in_id),
                self.ElementIds.phoneLengthError: Holder(driver.find_element_by_id, AndroidSignInPhoneNumber.error_text_id),

                self.ElementIds.heading_text: Holder(driver.find_element_by_id,
                                                         AndroidSignInPhoneNumber.heading_popup_id),


                self.ElementIds.passwordLengthError: Holder(driver.find_element_by_xpath, AndroidSignInPhoneNumber.password_error_text_xpath),
                self.ElementIds.phoneAndPasswordNotMatch: Holder(driver.find_element_by_id, AndroidSignInPhoneNumber.error_text_id),

                self.ElementIds.forgotPassword: Holder(driver.find_element_by_id,
                                                       AndroidSignInPhoneNumber.fogot_password_id),

                self.ElementIds.your_email: Holder(driver.find_element_by_xpath,
                                                   AndroidSignInPhoneNumber.your_email_xpath),

                self.ElementIds.your_cell_phone_number_forget_password: Holder(driver.find_element_by_id,
                                                                               AndroidSignInPhoneNumber.your_cell_phone_number_forget_password_id),

                self.ElementIds.reset_password: Holder(driver.find_element_by_id,
                                                       AndroidSignInPhoneNumber.reset_password_id),


            }
        elif platform == PlatformSupported.IOS:
            self.elements = {
                self.ElementIds.countryCode: Holder(driver.find_element_by_xpath, IOSSignIn.country_code_xpath),
                self.ElementIds.yourCellPhoneNumber: Holder(driver.find_element_by_xpath, IOSSignIn.your_cell_phone_number_xpath),
                self.ElementIds.password: Holder(driver.find_element_by_xpath, IOSSignIn.password_xpath),
                self.ElementIds.signIn: Holder(driver.find_element_by_id, IOSSignIn.sign_in),
                self.ElementIds.phoneLengthError: Holder(driver.find_element_by_id, IOSSignIn.enter_a_valid_cell),
                self.ElementIds.passwordLengthError: Holder(driver.find_element_by_id, IOSSignIn.password_length),
                self.ElementIds.phoneAndPasswordNotMatch: Holder(driver.find_element_by_id, IOSSignIn.do_not_match),

                self.ElementIds.signInWithEmail: Holder(driver.find_elements_by_class_name, IOSSignIn.sign_in_with_email_xpath),
                self.ElementIds.forgotPassword: Holder(driver.find_element_by_id,
                                                       IOSSignIn.forgot_password),
                self.ElementIds.your_cell_phone_number_forget_password: Holder(driver.find_element_by_xpath,
                                                                               IOSSignIn.your_cell_phone_number_forget_password_xpath),
                self.ElementIds.reset_password: Holder(driver.find_element_by_id,
                                                       IOSSignIn.reset_password),
                self.ElementIds.your_email: Holder(driver.find_element_by_xpath,
                                                   IOSSignIn.your_email_xpath),
                self.ElementIds.email_error: Holder(driver.find_element_by_id, IOSSignIn.enter_a_valid_email_id),
            }
        else:
            assert False, "Unknown platform {}".format(platform)