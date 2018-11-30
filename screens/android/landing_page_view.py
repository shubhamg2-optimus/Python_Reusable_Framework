from locators.locators import AndroidLandingPage as Locator
from screens.screen_base import Screen


class LandingPageView(Screen):

    def find_option_environment(self, environment="staging"):
        if environment == "production":
            return self.driver.find_element_by_xpath(Locator.prod_xpath)
        if environment == "staging":
            return self.driver.find_element_by_xpath(Locator.staging_xpath)
        if environment == "develop":
            return self.driver.find_element_by_xpath(Locator.develop_xpath)
        if environment == "trial":
            return self.driver.find_element_by_xpath(Locator.trial_xpath)
        if environment == "load":
            return self.driver.find_element_by_xpath(Locator.load_xpath)

    def find_button_cancel(self):
        return self.driver.find_element_by_xpath(Locator.cancel_xpath)

    def find_element_set(self):
        return self.driver.find_element_by_xpath(Locator.set_xpath)