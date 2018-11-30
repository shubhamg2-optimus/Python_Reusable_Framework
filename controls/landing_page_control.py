from screens.android.landing_page_view import LandingPageView

class LandingPage():

    def __init__(self, driver):
        self.page = LandingPageView(driver)

    def select_environment(self, environment):
        self.page.find_option_environment(environment).click()

    def confirm_environment(self):
        self.page.find_element_set().click()
