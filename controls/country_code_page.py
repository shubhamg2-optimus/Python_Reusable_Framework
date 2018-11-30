from screens.android.country_code_page_view import CountryCodePageView

class CountryCodePage():

    def __init__(self, driver):
        self.page = CountryCodePageView(driver)

    def select_code(self, code="united_states"):
        if code is "united_states":
            self.page.find_united_states().click()
        if code is "canada":
            self.page.find_canada().click()