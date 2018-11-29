from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.expected_conditions import element_to_be_clickable

_failed_expectations = []


class BasePage():

    default_timeout_time = 60

    def __init__(self, logger, webdriver):
        self.driver = webdriver
        self.saveto = logger

    def get_page_title(self):
        return self.driver.title

    def element_click_by_xpath(self, element_xpath):
        self.saveto.logger.info("%s is clicked" % element_xpath)
        self.wait(self.driver.find_element_by_xpath(element_xpath))
        self.driver.find_element_by_xpath(element_xpath).click()

    def elements_click_by_xpath(self, elements_xpath):
        self.saveto.logger.info("%s is clicked" % elements_xpath)
        elements = self.driver.find_elements_by_xpath(elements_xpath)
        for element in elements:
            element.click()

    def element_click_by_visible_text(self, element_visible_text):
        self.saveto.logger.info("%s is clicked" % element_visible_text)
        self.wait_till_element_is_clickable(self.driver.find_element_by_xpath("//*[contains(text(),'"+element_visible_text+"')]"))
        self.driver.find_element_by_xpath("//*[contains(text(),'"+element_visible_text+"')]").click()

    def element_click_by_link_text(self, element_link_text):
        self.saveto.logger.info("%s is clicked" % element_link_text)
        self.wait(self.driver.find_element_by_partial_link_text(element_link_text))
        self.driver.find_element_by_partial_link_text(element_link_text).click()

    def element_click_by_class(self, element_class):
        self.saveto.logger.info("Sign in button is clicked")
        self.wait(self.driver.find_element_by_class_name(element_class))
        self.driver.find_element_by_class_name(element_class).click()

    def select_list_element_by_text(self, element, text):
        self.saveto.logger.info("%s drop down is selected" % element.text)
        drop_down = Select(element)
        drop_down.select_by_visible_text(text)

    def is_checkbox_selected(self, element_xpath):
        self.saveto.logger.info("checking if checkbox is selected")
        return self.driver.find_element_by_xpath(element_xpath).is_selected()

    def is_text_present(self, text):
        self.saveto.logger.info("checking if text is present")
        return text in self.driver.page_source

    def wait(self, element):
        self.driverWait = WebDriverWait(self.driver, self.default_timeout_time)
        self.driverWait.until(visibility_of(element))

    def wait_till_element_is_clickable(self, element):
        self.driverWait = WebDriverWait(self.driver, self.default_timeout_time)
        self.driverWait.until(element_to_be_clickable(element))

    def check_exists(self, element_xpath):
        try:
            self.driver.find_element_by_xpath(element_xpath)
        except NoSuchElementException:
            return False
        return True

    def check_element_exists(self, element):
        try:
            element
        except NoSuchElementException:
            return False
        return True

    def check_not_exists(self, element_xpath):
        try:
            self.driver.find_element_by_xpath(element_xpath)
        except NoSuchElementException:
            return True
        return False

    def enter_value_in_text_field(self, element_id, value):
        self.wait(self.driver.find_element_by_id(element_id))
        self.saveto.logger.info("Clearing value from the text field")
        self.driver.find_element_by_id(element_id).clear()
        self.saveto.logger.info("Entering %s value in the text field" % value)
        self.driver.find_element_by_id(element_id).send_keys(value)

    def enter_value_in_text_field_by_xpath(self, element_xpath, value):
        self.saveto.logger.info("Clearing value from the text field")
        self.wait(self.driver.find_element_by_xpath(element_xpath))
        self.driver.find_element_by_xpath(element_xpath).clear()
        self.saveto.logger.info("Entering %s value in the text field" % value)
        self.driver.find_element_by_xpath(element_xpath).send_keys(value)

    def enter_value_in_text_field_by_id(self, element_id, value):
        self.saveto.logger.info("Clearing value from the text field")
        self.wait(self.driver.find_element_by_id(element_id))
        self.driver.find_element_by_id(element_id).clear()
        self.saveto.logger.info("Entering %s value in the text field" % value)
        self.driver.find_element_by_id(element_id).send_keys(value)

    def count_elements_with_xpath(self, element_xpath):
        return len(self.driver.find_elements_by_xpath(element_xpath))

    def get_text(self, element_xpath):
        self.saveto.logger.info("Getting text value")
        self.wait(self.driver.find_element_by_xpath(element_xpath))
        return self.driver.find_element_by_xpath(element_xpath).text

    def get_text_by_CSS(self, element_css):
        self.saveto.logger.info("Getting text value")
        self.wait(self.driver.find_element_by_css_selector(element_css))
        self.saevto.logger.info("value is "+ self.driver.find_element_by_css_selector(element_css).text)
        return self.driver.find_element_by_css_selector(element_css).text

    def get_attribute(self, element_xpath, attribute):
        self.saveto.logger.info("Getting attribute value")
        return self.driver.find_element_by_xpath(element_xpath).get_attribute(attribute)

    def get_value_of_css_property(self, element_xpath, property):
        self.saveto.logger.info("Getting value of css property")
        return self.driver.find_element_by_xpath(element_xpath).value_of_css_property(property)

    def perform_hover_by_xpath(self, element_xpath):
        self.saveto.logger.info("Hovering over the element")
        element_to_hover_over = self.driver.find_element_by_xpath(element_xpath)
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()

    def refresh_browser(self):
        self.saveto.logger.info("Refreshing browser")
        self.driver.refresh()