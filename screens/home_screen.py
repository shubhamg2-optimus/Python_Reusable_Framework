class HomeScreen():

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
    app_logo_id = "android:id/home"
    overflow_icon_class = "android.widget.ImageButton"
    first_name_text_field_id = "com.vector.guru99:id/first_name"
    last_name_text_field_id = "com.vector.guru99:id/last_name"
    email_address_text_field_id = "com.vector.guru99:id/email_address"
    comments_text_field_id = "com.vector.guru99:id/comment"
    send_button_id = "com.vector.guru99:id/send"


    def verify_logo(self):
        self.driver.find_element_by_id(self.app_logo_id).is_displayed()

    def navigate_to_contact_us(self):
        self.bs.element_click_by_class(self.overflow_icon_class)
        self.bs.element_click_by_visible_text("Contact Us")
        

