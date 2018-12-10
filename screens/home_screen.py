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
    app_logo_class = "android.widget.ImageView"
    app_logo_id = "android:id/home"
    overflow_icon_class = "android.widget.ImageButton"
    contact_us_class = "android.widget.LinearLayout"


    def verify_logo(self):
        self.driver.find_element_by_id(self.app_logo_id).is_displayed()

    def navigate_to_contact_us(self):
        self.bs.element_click_by_class(self.overflow_icon_class)
        self.bs.element_click_by_class(self.contact_us_class)


