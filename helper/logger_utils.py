import logging
import os


class Logger(object):
    def __init__(self, logger_name, use_existing=False, logger_level=logging.DEBUG):
        self.logger_name = logger_name

        if not use_existing:
            self.logger = logging.getLogger()
        else:
            self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logger_level)

        script_dir = os.path.dirname(__file__)

        # create a "logs" folder if it doesn't exist
        logs_path = os.path.abspath(os.path.join(script_dir, '../logs'))

        if not os.path.exists(logs_path):
            os.makedirs(logs_path, exist_ok=True)
        logs_path = os.path.abspath(os.path.join(script_dir, '../logs', self.logger_name))

        # create formatter and add it to the handlers
        formatter = logging.Formatter(fmt='%(asctime)s.%(msecs)03d: %(name)s: %(levelname)s: %(message)s',
                                      datefmt='%H:%M:%S')

        if not self.logger.handlers:
            # create file handler which logs even debug messages
            filelog = logging.FileHandler(logs_path)
            filelog.setLevel(logger_level)
            filelog.setFormatter(formatter)

            self.logger.addHandler(filelog)

            # create console handler with a higher log level
            consolelog = logging.StreamHandler()
            consolelog.setLevel(logger_level)
            consolelog.setFormatter(formatter)

            self.logger.addHandler(consolelog)

