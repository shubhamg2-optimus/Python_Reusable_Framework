from mobile_utils.constant import Data

class ContactUsScreen():

    def __init__(self, logger, driver, basescreen):
        """
        The first screen will be displayed after the application launches successfully.
        :param logger: The logger to log to
        :param driver: The web driver
        """
        self.logger = logger
        self.driver = driver
        self.bs = basescreen

    #Locators
    first_name_text_field_id = "com.vector.guru99:id/first_name"
    last_name_text_field_id = "com.vector.guru99:id/last_name"
    email_address_text_field_id = "com.vector.guru99:id/email_address"
    comments_text_field_id = "com.vector.guru99:id/comment"
    send_button_id = "com.vector.guru99:id/send"
    success_msg_xpath = "//*[text()='Message sent successfully!']"

    def send_query(self):
        self.bs.enter_value_in_text_field(self.first_name_text_field_id, Data.first_name)
        self.bs.enter_value_in_text_field(self.last_name_text_field_id, Data.last_name)
        self.bs.enter_value_in_text_field(self.email_address_text_field_id, Data.email_address)
        self.bs.enter_value_in_text_field(self.comments_text_field_id, Data.comment)
        self.driver.back()
        self.bs.element_click_by_id(self.send_button_id)

    def verify_success_msg(self):
        return self.bs.check_exists(self.success_msg_xpath)
