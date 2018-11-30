from screens.android.navigatioin_page_view import NavigationPageView

class NavigationPage():

    def __init__(self, driver):
        self.page = NavigationPageView(driver)

    def load_account_page(self):
        self.page.find_account_menu_button().click()