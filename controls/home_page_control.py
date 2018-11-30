from screens.android.home_page_view import HomePageView


class HomePage():
    def __init__(self, driver):
        self.page = HomePageView(driver)

    def load_navigation_page(self):
        self.page.find_navigation_button().click()