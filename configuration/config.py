# -*- coding: utf-8 -*-
from __future__ import absolute_import
from configobj import ConfigObj
import os


class MobileConfig():

    def __init__(self, config_file_name='config.ini'):
        script_dir = os.path.dirname(__file__)
        config = ConfigObj(script_dir + "/" + config_file_name)

        if os.environ.get('PYTHON_MOBILE_TEST_ENVIRONMENT') is not None:
            self.mode = os.environ.get('PYTHON_MOBILE_TEST_ENVIRONMENT')
        else:
            self.mode = config['environment']

        self.name = config[self.mode]['name']
        self.phonenumber = config[self.mode]['phonenumber']
        self.password = config[self.mode]['password']
        self.timeout = config['timeout']

        if os.environ.get('PYTHON_MOBILE_TEST_PLATFORM') is not None:
            self.platform = os.environ.get('PYTHON_MOBILE_TEST_PLATFORM')
        else:
            self.platform = config['platform']

        self.log = self.platform + "." + config[self.mode]['log']

        self.android_appium_version = config['android']["appium-version"]
        self.android_platformName = config['android']['platformName']
        self.android_platformVersion = config['android']['platformVersion']
        self.android_AutomationName = config['android']['AutomationName']
        self.android_deviceName = config['android']['deviceName']
        self.android_appPackage = config['android']['appPackage']
        self.android_appActivity = config['android']['appActivity']
        self.android_app = config['android']['app']
        self.android_noReset = config['android']['noReset']
        self.android_fullReset = config['android']['fullReset']