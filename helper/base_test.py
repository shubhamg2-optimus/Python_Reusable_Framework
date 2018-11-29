import unittest
from helper.logger_utils import Logger
from api.external_lib import jsonCompare

import json


class BaseTest(unittest.TestCase):
    """
    Base Test Case class to be used by all API test cases.
    """

    saveto = Logger("users.log")

    def verify_json_response(self, expected, actual):
        expected_json = json.loads(expected.text)
        actual_json = json.loads(actual.text)
        delta1 = jsonCompare.Diff(expected_json, actual_json).difference
        delta2 = jsonCompare.Diff(actual_json, expected_json).difference
        return delta1, delta2