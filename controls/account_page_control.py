from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from screens.android.account_page_view import AccountPageView


class AccountPage():

    def __init__(self, driver):
        self.page = AccountPageView(driver)
        self.wait = WebDriverWait(driver, 10)

    def load_log_out_container(self):
        self.page.find_logout_container_button().click()
        self.wait.until(EC.visibility_of(self.page.find_logout_confirm_button()));

    def confirm_log_out(self):
        self.page.find_logout_confirm_button().click()