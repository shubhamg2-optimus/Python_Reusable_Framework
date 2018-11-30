import types
import os

from utils.decorators import find_current_test_case_id

class Holder(object):
    def __init__(self, func, *args, index=None, country=None):
        self.func = [func]
        self.args = args
        self.index = index
        self.element = None
        self.country = country

    def get_element(self, logger, screenId, elementId, driver):

        if self.element is None:
            func = self.func[0]

            try:
                self.element = func(*self.args)
            except Exception:
                self._screenshot(logger, driver, screenId, elementId)
                raise

            if self.index is not None:
                try:
                    self.element = self.element[self.index]
                except Exception:
                    self._screenshot(logger, driver, screenId, elementId)
                    raise

            if self.country is not None:
                try:
                    result = [one for one in self.element if one.get_attribute("text") == self.country]
                    self.element = result[0]

                except Exception:
                    self._screenshot(logger, driver, screenId, elementId)
                    raise

            self._make_log_method(logger, screenId, elementId, "set_value", ["value"])
            self._make_log_method(logger, screenId, elementId, "click", [])

        return self.element

    def _make_log_method(self, logger, screenId, elementId, name, expected_args):
        """
        Wraps the given function on the element object so that each time
        this function is called, all function arguments are logged.

        :param logger: The logger to log to
        :param screenId: The name of the screen this element belogns to
        :param elementId: The ID of the element contained in this class
        :param name: The name of the function to wrap
        :param expected_args: The list of strings representing expected arguments
        """
        old_func = getattr(self.element, name)

        def _log_method(element, *args, **kwargs):
            logger.info("[{}:{}] Called {}() with [{}]".format(
                screenId,
                elementId,
                name,
                ", ".join([
                    "{}=\"{}\"".format(arg_name, args[i])
                    for i, arg_name in enumerate(expected_args)
                ]),
            ))

            return old_func(*args, **kwargs)

        _log_method.__name__ = name
        _log_method.__doc__ = old_func.__doc__

        setattr(self.element, name, types.MethodType(_log_method, self.element))

    def _screenshot(self, logger, driver, screenId, elementId):
        logger.info("[{}:{}] not found ".format(screenId, elementId))

        script_dir = os.path.dirname(__file__)

        # create a "screenshot" folder if it doesn't exist
        screenshots_path = os.path.abspath(os.path.join(script_dir, '../../screenshots'))

        if not os.path.exists(screenshots_path):
            os.makedirs(screenshots_path)
        caseId = find_current_test_case_id()
        screenshots_path = os.path.abspath(os.path.join(script_dir, '../../screenshots', caseId + "_" + screenId + "_"+ elementId + ".png"))
        driver.save_screenshot(screenshots_path)