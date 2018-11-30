import time
import unittest

from controls.preface_page_control import PrefacePage

from base_test import BastTest
from controls.landing_page_control import LandingPage
from utils.delayed_assert import expect, assert_expectations


class PromoSlidesTests(BastTest):

    def test_001_four_promo_slides(self):
        promopage = PrefacePage(self.driver)
        count = {"LocateYourCar": 0, "MonitorLovedOnes": 0, "Issues": 0, "DriveSmarter":0}

        for i in range(1, 50):
            try:
                text = promopage.view_center_text()

                if text == "Locate Your Car":
                    count.update({"LocateYourCar": count["LocateYourCar"] + 1})
                elif text == "Monitor Loved Ones":
                    count.update({"MonitorLovedOnes": count["MonitorLovedOnes"] + 1})
                elif text == "Issues":
                    count.update({"Issues": count["Issues"] + 1})
                elif text == "Drive Smarter":
                    count.update({"DriveSmarter": count["DriveSmarter"] + 1})
                else:
                    self.saveto.logger.debug("Found a new slide: %s" % text)
            except UnboundLocalError as e:
                self.saveto.logger.info("Handling run-time error: % " % e.message)

            time.sleep(0.1)

        self.saveto.logger.info(count)
        expect(count["LocateYourCar"] >= 1, "never played: Locate Your Car.")
        expect(count["MonitorLovedOnes"] >= 1, "never played: Monitor Loved Ones.")
        expect(count["Issues"] >= 1, "never played: Issues.")
        expect(count["DriveSmarter"] >= 1, "never played: Drive Smarter.")

        assert_expectations()

    def test_002_set_test_environment(self):
        promopage = PrefacePage(self.driver)
        time.sleep(20)
        promopage.load_landing_page()
        landingpage = LandingPage(self.driver)
        landingpage.select_environment("staging")
        landingpage.confirm_environment()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PromoSlidesTests)
    unittest.TextTestRunner(verbosity=2).run(suite)