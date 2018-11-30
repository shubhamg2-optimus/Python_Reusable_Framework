from appium import webdriver
import unittest, os
import time

from utils.logger import Logger
from configuration.config import MobileConfig
from screens.modes import PlatformSupported
from screens.first_screen import FirstScreen
from screens.select_environment_screen import SelectEnvironmentScreen

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class BaseTest(unittest.TestCase):

    mc = MobileConfig()
    email = mc.name
    password = mc.password
    phonenumber = mc.phonenumber
    log_name = mc.log
    platform = PlatformSupported(mc.platform)
    logger = Logger(log_name).logger

    def setUp(self):
        desired_caps = {}
        if self.platform == PlatformSupported.ANDROID:
            desired_caps['appium-version'] = self.mc.android_appium_version
            desired_caps['platformName'] = self.mc.android_platformName
            desired_caps['platformVersion'] = self.mc.android_platformVersion
            desired_caps['AutomationName'] = self.mc.android_AutomationName
            desired_caps['deviceName'] = self.mc.android_deviceName
            desired_caps['appPackage'] = self.mc.android_appPackage
            desired_caps['appActivity'] = self.mc.android_appActivity
            desired_caps['app'] = PATH('../../../Desktop/andriod_app/' + self.mc.android_app)
            desired_caps['noReset'] = self.mc.android_noReset
        else:
            assert False, "Unknown platform {}".format(self.platform)
        self.driver = webdriver.Remote(command_executor='http://0.0.0.0:4723/wd/hub', desired_capabilities=desired_caps)
        self.driver.implicitly_wait(self.mc.timeout)
        try:
            time.sleep(15)
            # self._choose_mode(self.mc.mode)
        except Exception:
            self.tearDown()
            raise

    def _choose_mode(self, mode):
        # Select the environment to start your test
        if self.platform == PlatformSupported.ANDROID:
            first_screen = FirstScreen(self.logger, self.driver, self.platform)

            for i in range(1, 8):
                # Tap the secret area to launch the select environment screen
                first_screen.click_environemnt(self.logger, self.driver)

            select_environment_screen = SelectEnvironmentScreen(self.logger, self.driver, self.platform)
            select_environment_screen.getElement(select_environment_screen.ElementIds(mode), driver=self.driver).click()
            select_environment_screen.getElement(select_environment_screen.ElementIds.Set, driver=self.driver).click()

    def tearDown(self):
        self.driver.quit()