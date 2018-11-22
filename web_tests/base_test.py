import unittest
import os

from configuration.config import OSConfig
from selenium import webdriver
from configuration.browsers import BrowserSupported
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pages.base_page import BasePage
import time
from utils.logger_utils import Logger
from pages.delayed_assert import DelayedAssert
from pages.Amazon.home_page import HomePage
from pages.Amazon.your_orders_page import YourOrdersPage
from pages.Amazon.sign_in_page import SignInPage
from web_helper.credential_helper import CredentialHelper
from pages.Amazon.your_account_page import YourAccountPage
from pages.Amazon.login_and_security_page import LoginAndSecurityPage


class BaseTest(unittest.TestCase):

    config = OSConfig()
    browser = BrowserSupported(config.browser)
    url = config.url

    logger = Logger(__name__ + ".log")

    @classmethod
    def setUpClass(cls):
        if cls.browser == BrowserSupported.CHROME:
            options = webdriver.ChromeOptions()
            options.add_argument("--kiosk")
            options.add_argument("allow-running-insecure-content")
            cls.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
            cls.driver.implicitly_wait(20)

        elif cls.browser == BrowserSupported.FIREFOX:
            options = webdriver.FirefoxOptions()
            options.add_argument("--kiosk")
            options.add_argument("allow-running-insecure-content")
            cls.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_options=options)
            cls.driver.implicitly_wait(20)

        else:
            assert False, "Unknown Browser {}".format(cls.browser)

        # Setting implicit wait
        cls.driver.implicitly_wait(20)

        # Navigating to sign in page
        cls.get_page_and_load_time(cls)

        # Creating objects for different pages
        cls.bp = BasePage(cls.logger, cls.driver)
        cls.da = DelayedAssert(cls.logger, cls.driver)

        cls.hp = HomePage(cls.logger, cls.driver, cls.bp)
        cls.yop = YourOrdersPage(cls.logger, cls.driver, cls.bp)
        cls.sip = SignInPage(cls.logger, cls.driver, cls.bp)
        cls.yap = YourAccountPage(cls.logger, cls.driver, cls.bp)
        cls.lasp = LoginAndSecurityPage(cls.logger, cls.driver, cls.bp)
        cls.ch = CredentialHelper()

    @staticmethod
    def get_page_and_load_time(cls):
        startTime = time.time()
        cls.driver.get(cls.url)
        endTime = time.time()
        cls.logger.logger.info("Page load time taken in: %s ms" % (endTime-startTime))

    @classmethod
    def tearDownClass(cls):
        if (cls.driver!=None):
            cls.driver.quit()

    def tearDown(self):
        self.da.assert_expectations()
        for method, error in self._outcome.errors:
            if error:
                if 'assert_expectations' not in str(error):
                    self.logger.logger.info("Taking Snapshot for the test case failure")
                    self.driver.save_screenshot(os.path.join(os.path.dirname(__file__), 'Snapshot', self._testMethodName + "_error.png"))