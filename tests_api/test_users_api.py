from __future__ import absolute_import

from api.external_lib.delayedAssert import expect, assert_expectations

import json

from api.lib.apiuser import ApiUser
from api.data.constants import Constants as C
from helper.base_test import BaseTest


class TestUsers(BaseTest):

    @classmethod
    def setUpClass(cls):
        cls.apir = ApiUser()

    def tearDown(self):
        assert_expectations(failtest=False)

    def test_001_get_users_call(self):
        # Getting users detail by calling GET /api/users
        resp = self.apir.get_users()

        # Verifying the response code
        expect(resp.status_code == C.SUCCESS_RESPONSE_CODE,
               "Incorrect Response Code. Expected: %s. Received: %s" % (C.SUCCESS_RESPONSE_CODE, resp.status_code))

        # Verifying the data returned contains an expected field
        jesp = json.loads(resp.text)
        expect("first_name" in jesp["data"][0].keys(), "first_name field is missing from the response")

    def test_002_get_users_call_for_non_existing_user(self):
        # Getting users detail by calling GET /api/users
        resp = self.apir.get_users_id("100")

        # Verifying the response code
        expect(resp.status_code == C.NOT_FOUND_RESPONSE_CODE,
               "Incorrect Response Code. Expected: %s. Received: %s" % (C.NOT_FOUND_RESPONSE_CODE, resp.status_code))

        # Verifying the data returned is empty
        jesp = json.loads(resp.text)
        expect(len(jesp) == 0, "Response data is not empty")

    def test_003_put_users_call(self):
        # Getting users detail by calling PUT /api/users
        resp = self.apir.put_users_id(C.EXISTING_USER_ID, payload=C.NEW_USER_PAYLOAD)

        # Verifying the response code
        expect(resp.status_code == C.SUCCESS_RESPONSE_CODE,
               "Incorrect Response Code. Expected: %s. Received: %s" % (C.SUCCESS_RESPONSE_CODE, resp.status_code))

        # Verifying the data returned contains the given field
        jesp = json.loads(resp.text)
        expect(C.NEW_USER_PAYLOAD["name"] == jesp["name"],
               "Updated name is not returned. Expected: %s. Received: %s" % (C.NEW_USER_PAYLOAD["name"], jesp["name"]))

    def test_004_delete_users_call(self):
        # Getting users detail by calling PUT /api/users
        resp = self.apir.delete_users_id(C.EXISTING_USER_ID)

        # Verifying the response code
        expect(resp.status_code == C.SUCCESS_NO_DATA_RESPONSE_CODE,
               "Incorrect Response Code. Expected: %s. Received: %s" % (
                C.SUCCESS_NO_DATA_RESPONSE_CODE, resp.status_code))

        # Verifying the data returned is empty
        expect(len(resp.text) == 0, "Response data is not empty")
