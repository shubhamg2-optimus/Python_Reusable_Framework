from mobile_tests.base_test import BaseTest


class SignInTest(BaseTest):

    def test_001_app_logo(self):
        self.assertTrue(self.hp.verify_logo(), "Guru99 logo is not displayed")

    def test_002_sending_query(self):
        self.hp.navigate_to_contact_us()
        self.cus.send_query()
        self.assertTrue(self.cus.verify_success_msg(), "Query sent success message is not displayed")