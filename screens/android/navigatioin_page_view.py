from locators.locators import AndroidNavigationPage as Locator
from screens.screen_base import Screen


class NavigationPageView(Screen):

    def find_account_menu_button(self):
        return self.driver.find_element_by_id(Locator.menu_button_id)