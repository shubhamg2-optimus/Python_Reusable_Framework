from screens.modes import PlatformSupported
from screens.elements.holder import Holder
from screens.screen_base import ScreenBase
from locators.locators import AndroidLandingPage
import enum

class SelectEnvironmentScreen(ScreenBase):
    @enum.unique
    class ElementIds(enum.Enum):
        # Common elements shared by both platforms
        Production = "production"
        Staging = "staging"
        Develop = "develop"
        Trial = "trial"
        Load = "load"
        Cancel = "cancel"
        Set = "set"

    def __init__(self, logger, driver, platform):
        """
        The first screen will be displayed after the application launches successfully.

        :param logger: The logger to log to
        :param driver: The web driver
        :param platform: The platform that automation will run on
        """

        super().__init__(logger, platform)

        if platform == PlatformSupported.ANDROID:
            # Holds all environments plus the confirm and cacel elements for the current screen on android
            # key is the ElementId: value is web element
            self.elements = {
                self.ElementIds.Production: Holder(driver.find_element_by_xpath, AndroidLandingPage.prod_xpath),
                self.ElementIds.Staging: Holder(driver.find_element_by_xpath, AndroidLandingPage.staging_xpath),
                self.ElementIds.Develop: Holder(driver.find_element_by_xpath, AndroidLandingPage.develop_xpath),
                self.ElementIds.Trial: Holder(driver.find_element_by_xpath, AndroidLandingPage.trial_xpath),
                self.ElementIds.Load: Holder(driver.find_element_by_xpath, AndroidLandingPage.load_xpath),
                self.ElementIds.Cancel: Holder(driver.find_element_by_xpath, AndroidLandingPage.cancel_xpath),
                self.ElementIds.Set: Holder(driver.find_element_by_xpath, AndroidLandingPage.set_xpath)
            }
        elif platform == PlatformSupported.IOS:
            # Holds all environments for the current screen on ios
            # key is the ElementId: value is web element
            self.elements = {
                self.ElementIds.Production: Holder(driver.find_element_by_xpath, AndroidLandingPage.prod_xpath, index=0),
                self.ElementIds.Staging: Holder(driver.find_element_by_xpath, AndroidLandingPage.staging_xpath, index=0),
                self.ElementIds.Develop: Holder(driver.find_element_by_xpath, AndroidLandingPage.develop_xpath, index=0),
                self.ElementIds.Trial: Holder(driver.find_element_by_xpath, AndroidLandingPage.trial_xpath, index=0),
                self.ElementIds.Load: Holder(driver.find_element_by_xpath, AndroidLandingPage.load_xpath, index=0),
            }
        else:
            assert False, "Unknown platform {}".format(platform)