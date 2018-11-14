import inspect
import os.path

_failed_expectations = []


class DelayedAssert():

    default_timeout_time = 60

    def __init__(self, logger, webdriver):
        self.driver = webdriver
        self.saveto = logger

    def expect(self, expr, msg=None):
        'keeps track of failed expectations'
        if not expr:
            self.saveto.logger.info("Taking Snapshot for the test case failure")
            if '.' in msg:
                self.driver.save_screenshot('../Snapshot/' + msg.split(".")[0] + "_error.png")
            else:
                self.driver.save_screenshot('../Snapshot/' + msg + "_error.png")
            self._log_failure(msg)

    def assert_expectations(self, failtest=True):
        'raise an assert if there are any failed expectations'
        if _failed_expectations:
            if failtest:
                assert False, self._report_failures()
            else:
                self._report_failures()

    def _log_failure(self, msg=None):
        (filename, line, funcname, contextlist) = inspect.stack()[2][1:5]
        filename = os.path.basename(filename)
        context = contextlist[0]
        _failed_expectations.append('file "%s", line %s, in %s()%s\n%s' %
                                    (filename, line, funcname, (('\n%s' % msg) if msg else ''), context))

    def _report_failures(self):
        global _failed_expectations
        if _failed_expectations:
            (filename, line, funcname) = inspect.stack()[2][1:4]
            report = [
                '\n\nassert_expectations() called from',
                '"%s" line %s, in %s()\n' % (os.path.basename(filename), line, funcname),
                'Failed Expectations:%s\n' % len(_failed_expectations)]
            for i, failure in enumerate(_failed_expectations, start=1):
                report.append('%d: %s' % (i, failure))
            _failed_expectations = []
        return ('\n'.join(report))