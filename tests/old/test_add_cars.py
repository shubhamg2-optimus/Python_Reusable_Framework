from controls_old.country_code_page import CountryCodePage
from controls_old.home_page_control import HomePage
from controls_old.landing_page_control import LandingPage
from controls_old.preface_page_control import PrefacePage
from controls_old.signin_phone_page_control import SignInPhoneNumberPage

from base_test import BastTest


class AddcarsTest(BastTest):

    def test_add_cars(self):

        # Step 1: Choose environment to run the test against
        promopage = PrefacePage(self.driver)

        promopage.load_landing_page()
        landingpage = LandingPage(self.driver)
        landingpage.select_environment("staging")
        landingpage.confirm_environment()

        # Step 2: Sign in with an existing correct phone number and password
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
        #
        # navigation_page = NavigationPage(self.driver)
        # navigation_page.load_account_page()
        #
        # account_page = AccountPage(self.driver)
        # account_page.load_log_out_container()
        # account_page.confirm_log_out()