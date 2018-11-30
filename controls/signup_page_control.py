from screens.android.signup_page_view import SignUpPageView

class SignUpPage():

    def __init__(self, driver):
        self.page = SignUpPageView(driver)
        self.driver = driver

    def load_country_code_page(self):
        return self.page.find_country_code().click()

    def type_phone_number(self, phone_number):
        self.page.find_field_cell_phone_number().set_value(phone_number)

    def type_email_address(self, email_address):
        self.page.find_field_email_address().set_value(email_address)

    def type_password(self, password):
        self.page.find_field_password().set_value(password)

    def click_agree_checkbox(self):
        self.page.find_checkbox_agree().click()

    def scroll_down_to_enable_accept_button_for_agreement(self):
        size = self.driver.get_window_size()

        for i in range(0, 50):
            # startY point at bottom of screen
            startY = size["height"] * 0.65

            # endY pint at top of screen
            endY = size["height"] * 0.01

            # horizontal part of screen where you want to start swipe
            startX = size["width"] / 2

            self.driver.swipe(startX, startY, startX, endY, 500)

    def click_accept_button(self):
        self.page.find_accept_button().click()

    def click_signup_button(self):
        self.page.find_signup_button().click()

    def type_pin_number(self, position, pin):
        self.page.find_pin(position).set_value(pin)

    def type_imei_number(self, position, code):
        self.page.find_code(position).set_value(code)

    def click_enter_code_manually(self):
        self.page.find_enter_code_manually().click()

    def click_continue_imei(self):
        self.page.find_imei_continue().click()

    def click_continue_sim_card(self):
        self.page.find_insert_sim_card_continue().click()

    def click_continue_install_device(self):
        self.page.find_install_device_continue().click()

    def click_cancel_connecting_to_your_car(self):
        self.page.find_cancel_connecting_device().click()

    def click_confirm_discard_device_activation_button(self):
        self.page.find_confirm_discard_device_activation_button().click()