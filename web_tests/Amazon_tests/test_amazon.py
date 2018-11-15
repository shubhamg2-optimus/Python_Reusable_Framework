from web_tests.base_test import BaseTest


class TestAccountDetails(BaseTest):

    def test_001_login_with_valid_credentials(self):
        self.hp.navigate_to_sign_in_page()
        self.sip.login_with_email_password(self.ch.valid_email, self.ch.valid_password)
        act_username = self.hp.get_username()
        self.assertEqual(self.ch.username, act_username, "Incorrect Username")

    def test_002_your_orders_section_for_a_new_account(self):
        self.hp.navigate_to_your_orders_page()
        self.bp.is_text_present(self.yop.NO_ORDER_TEXT)
