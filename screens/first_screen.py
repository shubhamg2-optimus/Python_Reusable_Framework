import enum

from locators.locators import AndroidFirstScreen
from screens.modes import PlatformSupported
from screens.elements.holder import Holder
from screens.screen_base import ScreenBase

class FirstScreen(ScreenBase):
    @enum.unique
    class ElementIds(enum.Enum):
        # Common elements shared by both platforms
        SignIn = "Sign In"
        SignUp = "Sign Up"
        LocateYourCar = "Locate Your Car"
        MonitorYourLovedOnes = "Monitor Your Loved Ones"
        CareForYourCar= "Car For Your Car"
        DriveSmarter = "Drive Smarter"

    def __init__(self, logger, driver, platform):
        """
        The first screen will be displayed after the application launches successfully.

        :param logger: The logger to log to
        :param driver: The web driver
        :param platform: The platform that automation will run on
        """
        super().__init__(logger, platform)

        if platform == PlatformSupported.ANDROID:
            # Holds all elements for the current screen on android
            # key is the ElementId: value is web element
            self.elements = {
                self.ElementIds.SignIn: Holder(driver.find_element_by_id, AndroidFirstScreen.signIn),
                self.ElementIds.SignUp: Holder(driver.find_element_by_xpath, AndroidFirstScreen.signUp_xpath),
            }
        elif platform == PlatformSupported.IOS:
            # Holds all elements for the current screen on android
            # key is the ElementId: value is web element
            self.elements = {
                self.ElementIds.SignIn: Holder(driver.find_elements_by_accessibility_id, IOSFirstScreen.signIn_id, index=0),
                self.ElementIds.SignUp: Holder(driver.find_elements_by_accessibility_id, IOSFirstScreen.signUp_id, index=0),
            }
        else:
            assert False, "Unknown platform {}".format(platform)

    def click_environemnt(self, logger, driver):
        if self.platform == PlatformSupported.ANDROID:
            # secret place to tap to launch the choose environment on android
            logger.info("[{}] Tapping at (524,283)".format(self.__class__.__name__))
            driver.tap([(524, 283)], 300)
        else:
            assert False, "Unknown platform {}".format(self.platform)
