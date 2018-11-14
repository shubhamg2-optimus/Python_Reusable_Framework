from __future__ import absolute_import
from Locators.locator import locator
from configuration.config_getter import config_getter
import os
import configparser


class OSConfig():

    def __init__(self, config_file_name='configuration.ini'):

        script_dir = os.path.dirname(__file__)
        config = configparser.ConfigParser()
        config.read(script_dir + "/" + config_file_name)

        configgetter = config_getter(config)
        self.platform = configgetter.getplatform()
        self.browser = configgetter.getbrowser()
        self.driver_location = config[self.browser]['driver_location']
        self.chrome_filename = config[self.browser]['chrome_filename']

        self.url = locator.base_url_amazon