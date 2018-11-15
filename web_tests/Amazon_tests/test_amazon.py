from web_tests.base_test import BaseTest


class TestAccountDetails(BaseTest):

    def test_001_login_with_valid_credentials(self):
        self.hp.navigate_to_sign_in_page()
        self.sip.login_with_email_password("amazon14nov2018@gmail.com", "Amazon123")