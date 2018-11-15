from web_tests.base_test import BaseTest


class TestAccountDetails(BaseTest):

    def test_001_login_with_valid_credentials(self):
        self.hp.navigate_to_sign_in_page()
        self.sip.login_with_email_password("amazon14nov2018@gmail.com", "Amazon123")

    def test_003_empty_username_field(self):
        self.hp.navigate_to_sign_in_page()
        self.sip.login_with_empty_email_id("")
        act_validation_msg = self.bp.get_text(self.sip.empty_email_validation_msg_xpath)
        self.assertEqual(act_validation_msg, self.sip.empty_email_validation_msg, "Invalid Error message")