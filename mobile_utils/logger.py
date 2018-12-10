import logging
import os

class Logger(object):
    def __init__(self, logger_name, use_existing=False, logger_level=logging.DEBUG):
        self.logger_name = logger_name

        if use_existing:
            self.logger = logging.getLogger()
        else:
            self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logger_level)

        # create file handler which logs even debug messages
        script_dir = os.path.dirname(__file__)

        # create a "logs" folder if it doesn't exist
        logs_path = os.path.abspath(os.path.join(script_dir, '../logs'))

        if not os.path.exists(logs_path):
            os.makedirs(logs_path)
        logs_path = os.path.abspath(os.path.join(script_dir, '../logs', self.logger_name))

        filelog = logging.FileHandler(logs_path)
        filelog.setLevel(logger_level)

        # create console handler with a higher log level
        consolelog = logging.StreamHandler()
        consolelog.setLevel(logger_level)

        # create formatter and add it to the handlers
        formatter = logging.Formatter(fmt='%(asctime)s.%(msecs)03d: %(name)s: %(levelname)s: %(message)s',
                                      datefmt='%H:%M:%S')
        filelog.setFormatter(formatter)
        consolelog.setFormatter(formatter)

        # add the handlers to logger
        self.logger.addHandler(consolelog)
        self.logger.addHandler(filelog)
