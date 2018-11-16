class YourOrdersPage():

    def __init__(self, logger, webdriver, base_page):
        self.saveto = logger
        self.bp = base_page
        self.driver = webdriver

    # Locators

    # Constants
    NO_ORDER_TEXT = "You have not placed any orders"

    # Functions