import os

class config_getter():

    def __init__(self, config):
        self._config = config

    def getplatform(self):
        if os.environ.get('PYTHON_WEB_TEST_PLATFORM') is not None:
            return os.environ.get('PYTHON_WEB_TEST_PLATFORM')
        else:
            return self._config['setup']['platform']

    def getbrowser(self):
        if os.environ.get('PYTHON_WEB_TEST_BROWSER') is not None:
            return os.environ.get('PYTHON_WEB_TEST_BROWSER')
        else:
            return self._config['setup']['browser']
