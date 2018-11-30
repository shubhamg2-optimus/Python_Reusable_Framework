from screens.modes import PlatformSupported
from screens.elements.holder import Holder
from screens.screen_base import ScreenBase
from locators.locators import AndroidCountryCode
import enum


class CountryCodeScreen(ScreenBase):
    @enum.unique
    class ElementIds(enum.Enum):
        # Common elements shared by both platforms
        Canada = "Canada"
        CzechRepublic = "Czech Republic"
        UnitedStates = "United States"

    def __init__(self, logger, driver, platform):
        """
        The first screen will be displayed after the application launches successfully.

        :param logger: The logger to log to
        :param driver: The web driver
        :param platform: The platform that automation will run on
        """

        super().__init__(logger, platform)

        if platform == PlatformSupported.ANDROID:
            self.elements = {
                self.ElementIds.Canada: Holder(driver.find_elements_by_class_name, AndroidCountryCode.united_states_type, country=self.ElementIds.Canada.value),
                self.ElementIds.UnitedStates: Holder(driver.find_elements_by_class_name, AndroidCountryCode.united_states_type, country=self.ElementIds.UnitedStates.value),
                self.ElementIds.CzechRepublic: Holder(driver.find_elements_by_class_name, AndroidCountryCode.united_states_type, country=self.ElementIds.CzechRepublic.value)
            }
        elif platform == PlatformSupported.IOS:
            self.elements = {
                self.ElementIds.Canada: Holder(driver.find_element_by_id, IOSSignIn.canada_id),
                self.ElementIds.UnitedStates: Holder(driver.find_element_by_id, IOSSignIn.united_states_id),
            }
        else:
            assert False, "Unknown platform {}".format(platform)