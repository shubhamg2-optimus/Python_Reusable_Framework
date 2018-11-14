import time
from pages.delayed_assert import DelayedAssert


class AccountDetailsPage():

    def __init__(self, logger, webdriver, base_page):
        self.saveto = logger
        self.bp = base_page
        self.driver = webdriver

    # Locators
    page_title_xpath = "//p-header"
    delete_icon_xpath = "//a[@class='icon trash']"
    duplicate_username_validation_xpath = './/*[text()="An account already exists with this username."]'
    special_characters_username_validation_xpath = ".//*[text()='The field UserName may only include letters, numbers and dashes.']"
    username_length_validation_xpath = './/*[text()="The field UserName must be a string with a minimum length of 6 and a maximum length of 32."]'
    email_xpath = './/*[text()="Email"]'
    phone_xpath = './/*[text()="Phone"]'
    language_xpath = './/*[text()="Language"]'
    units_xpath = './/*[text()="Units"]'
    name_xpath = './/*[text()="Name"]'
    name_textbox_xpath = './/*[@class="ui-g-12 row"]/div[text()="field"]/../div[2]/span'
    your_account_xpath = ".//*[text()='Your Account']"
    your_devices_xpath = ".//*[text()='Your Devices']"
    your_cars_xpath = ".//*[text()='Your Cars']"
    version_number_xpath = "//div[@class= 'version']"
    imei_xpath = ".//*[text()='IMEI']"
    connected_xpath = ".//*[text()='Connected']"
    tick_mark_button_xpath = ".//*[@style='display: inherit;']/div[1]"
    cross_mark_button_xpath = ".//*[@style='display: inherit;']/div[2]"
    user_info_field_area_xpath = ".//*[text()='field']/parent::div/div[2]"
    dropdown_field_xpath = "//*[text()='field']/parent::div/span"
    close_button_xpath = "//*[contains(@class, 'dialog-account-details')]//a"
    get_email_xpath = ".//*[text()='field']/parent::div/div[2]/span"
    user_data_update_msg_xpath = ".//*[@class='ui-growl-message']/p"
    name_err_msg_xpath = "//*[@class='error-message ng-star-inserted']/div"
    email_err_msg_xpath = "//*[@class='error-message ng-star-inserted']"
    edit_field_xpath = ".//*[@style='display: inherit;']/input"
    duplicate_email_validation_xpath = ".//*[text()='An account already exists with this email.']"
    invalid_email_xpath = ".//*[text()='The Email field is not a valid e-mail address.']"
    unclaim_device_button_xpath = "//*[text()='Unclaim Device']"
    cancel_button_xpath = ".//a[text()='Cancel']"
    device_xpath = ".//div[@class='ui-g-12 ui-lg-6 ui-g-nopad device']"
    imei_number_xpath = ".//div[@class='ui-g-8']//label"
    select_imei_checkbox_xpath = ".//*[@class='ui-chkbox-box ui-widget ui-corner-all ui-state-default']"
    unselect_imei_checkbox_xpath = ".//*[@class='ui-chkbox-icon ui-clickable fa fa-check']"
    connection_status_xpath = "//div[@class='ui-g-4 true ng-star-inserted']"
    delete_confirmation_cancel_button_xpath = "//*[@class='ui-dialog-footer ui-widget-content ng-tns-c7-3']/p-footer/button[1]"
    delete_confirmation_no_button_xpath = ".//*[@class='undefined ui-button ui-widget ui-state-default ui-corner-all ui-button-text-icon-left']/span[text()='No']"
    delete_confirmation_yes_button_xpath = ".//*[@class='ui-dialog-footer ui-widget-content ng-tns-c7-3']//p-footer/button[2]"
    car_in_car_section_xpath = "//app-vehicle-display[@class='app-vehicle-display']/div/img"
    issue_count_xpath = "//app-vehicle-display[@class='app-vehicle-display']/div/div/div"
    car_satus_xpath = "//app-vehicle-display[@class='app-vehicle-display']/div"
    dropdown_expand_icon_xpath = "//*[contains(@class,'ui-dropdown-trigger-icon ui-clickable fa fa-fw fa-caret-down')]"
    select_language_xpath = "//*[contains(@class,'ui-dropdown-items ui-dropdown-list')]//span[text()='language']"

    # Constants
    duplicate_username_error_message = 'An account already exists with this username.'
    duplicate_email_message = "An account already exists with this email."
    duplicate_phone_number_message = "An account already exists with this phone number."
    phone_number_length_message = "Phone number must have minimum length of 7 and a maximum length of 15."
    invalid_phone_number_msg = " is not a valid phone number. Make sure your country code is correct or contact Mojio support for assistance."
    special_characters_name_message = 'The field Name may only include letters, numbers and dashes.'
    exp_empty_name_msg = "Name is required"
    username_length_validation_message = 'The field UserName must be a string with a minimum length of 6 and a maximum length of 32.'
    firstname_length_validation_message = 'The field FirstName must be a string with a maximum length of 50.'
    lastname_length_validation_message = "The field LastName must be a string with a maximum length of 50."
    successful_update_info_msg = "User data updated successfully"
    error_info_msg = "The field Name may only include alphanumeric characters."
    select_device_info_msg = "Please select a device to delete"
    deleted_device_info_msg = "Device deleted"
    updating_info_msg = "Updating..."
    invalid_email_message = "The Email field is not a valid e-mail address."
    red_color = "rgb(255, 255, 255)"
    username_field_length = "32"
    offline_car_status = "car-status-offline"
    supported_languages = ["Czech", "French", "German", "Spanish", "English"]
    language = ["Language", "Jazyk", "Langue", "Sprache", "Idioma"]
    exp_page_title = {"English":"Account Details", "Czech":"Podrobnosti o účtu", "French":"Détails du compte", "German":"Kontodetail", "Spanish":"Detalle de la cuenta"}

    # Script
    get_color_script = "return window.getComputedStyle(document.querySelector('html>body>div>div>perfect-scrollbar>div>div>div>div>div>div>div>div>div>div>app-vehicle-display>div>div>div','$0')).getPropertyValue('color');"

    # Functions
    def update_user_information(self, field, value):
        time.sleep(5)
        self.bp.element_click_by_xpath(self.user_info_field_area_xpath.replace("field", field))
        self.bp.enter_value_in_text_field_by_xpath(self.edit_field_xpath, value)
        self.bp.element_click_by_xpath(self.tick_mark_button_xpath)
        time.sleep(5)

    def verify_user_info_update_msg(self, exp_message):
        act_message = self.bp.get_text(self.user_data_update_msg_xpath)
        DelayedAssert.expect(act_message == exp_message, "User data update msg is missing. Received: %s. Expected: %s" % (act_message, exp_message))

    def verify_vehicle_icon_color(self, color):
        content = self.driver.execute_script(self.get_color_script)
        if color == "red":
            color = self.red_color
            DelayedAssert.expect(content == color,
               "Incorrect color for vehicle icon is displayed. Expected: %s. Received: %s" % (color, content))

    def edit_user_info(self, field, value):
        time.sleep(5)
        self.bp.element_click_by_xpath(self.user_info_field_area_xpath.replace("field", field))
        self.bp.enter_value_in_text_field_by_xpath(self.edit_field_xpath, value)
        self.bp.element_click_by_xpath(self.cross_mark_button_xpath)
        time.sleep(15)

    def verify_error_msg(self, msg):
        act_err_msg = self.bp.get_text(self.name_err_msg_xpath)
        DelayedAssert.expect(act_err_msg == msg, "Incorrect error msg. Received: %s Expected: %s" % (act_err_msg, msg))

    def verify_email_error_msg(self, msg):
        act_err_msg = self.bp.get_text(self.email_err_msg_xpath)
        DelayedAssert.expect(act_err_msg == msg, "Incorrect error msg. Received: %s Expected: %s" % (act_err_msg, msg))
