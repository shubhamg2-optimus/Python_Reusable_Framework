from locators.locators import AndroidHomePage as Xpath
from screens.screen_base import Screen


class HomePageView(Screen):

    def find_navigation_button(self):
        return self.driver.find_element_by_xpath(Xpath.navigation_drawer_xpath)