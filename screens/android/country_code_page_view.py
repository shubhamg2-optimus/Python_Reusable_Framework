from locators.locators import AndroidCountryCode as Xpath
from screens.screen_base import Screen


class CountryCodePageView(Screen):

    def find_go_back_arrow(self):
        return self.driver.find_element_by_xpath(Xpath.back_xpath)

    def find_canada(self):
        return self.driver.find_element_by_xpath(Xpath.canada_xpath)

    def find_united_states(self):
        return self.driver.find_element_by_xpath(Xpath.united_states_type)