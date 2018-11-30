class ScreenBase(object):

    def __init__(self, logger, platform):
        self.logger = logger
        self.platform = platform
        self.elements = {}

    def getElement(self, elementId, driver):
        return self.elements[elementId].get_element(self.logger, self.__class__.__name__, elementId.name, driver)