from locators.locators import AndroidAccountPageId as Locator
from screens.screen_base import Screen


class AccountPageView(Screen):

    def find_logout_container_button(self):
        return self.driver.find_element_by_id(Locator.logout_container_id)

    def find_logout_confirm_button(self):
        return self.driver.find_element_by_id(Locator.logout_dialog_confirm_button_id)