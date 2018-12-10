from appium import webdriver
import unittest, os

from mobile_utils.logger import Logger
from mobile_configuration.config import MobileConfig
from screens.home_screen import HomeScreen
from screens.base_screen import BaseScreen
from screens.contact_us_screen import ContactUsScreen
from mobile_utils.delayed_assert import DelayedAssert

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class BaseTest(unittest.TestCase):

    mc = MobileConfig()
    email = mc.name
    password = mc.password
    phonenumber = mc.phonenumber
    log_name = mc.log
    logger = Logger(log_name)

    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps['appium-version'] = cls.mc.android_appium_version
        desired_caps['platformName'] = cls.mc.android_platformName
        desired_caps['platformVersion'] = cls.mc.android_platformVersion
        desired_caps['AutomationName'] = cls.mc.android_AutomationName
        desired_caps['deviceName'] = cls.mc.android_deviceName
        desired_caps['appPackage'] = cls.mc.android_appPackage
        desired_caps['appActivity'] = cls.mc.android_appActivity
        desired_caps['app'] = PATH(cls.mc.android_app)
        desired_caps['noReset'] = cls.mc.android_noReset

        cls.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
        cls.driver.implicitly_wait(cls.mc.timeout)

        # Creating objects for different pages
        cls.bs = BaseScreen(cls.logger, cls.driver)
        cls.hp = HomeScreen(cls.logger, cls.driver, cls.bs)
        cls.cus = ContactUsScreen(cls.logger, cls.driver, cls.bs)
        cls.da = DelayedAssert(cls.logger, cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
