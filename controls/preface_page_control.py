from screens.first_screen import FirstScreen


class PrefacePage():

    def __init__(self, driver):
        self.page = FirstScreen(driver)
        self.driver = driver

    def click_signIn(self):
        self.page.find_button_signIn().click()

    def click_signUp(self):
        self.page.find_button_signUp().click()

    def view_center_text(self):
        return self.page.find_center_text().text

    def load_landing_page(self):
        for i in range(1, 8):
            self.driver.tap([(524, 283)], 300)