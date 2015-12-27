import logging
import os
from anybox.nose_selenium.selenium import SeleniumTestCase
from selenium_extra.driver import Driver
from nose.plugins import Plugin
from nose.loader import TestLoader

log = logging.getLogger(__name__)
# on SkipTest:
#  - unittest SkipTest is first preference, but it's only available
#    for >= 2.7
#  - unittest2 SkipTest is second preference for older pythons.  This
#    mirrors logic for choosing SkipTest exception in testtools
#  - if none of the above, provide custom class
try:
    from unittest.case import SkipTest
except ImportError:
    try:
        from unittest2.case import SkipTest
    except ImportError:
        class SkipTest(Exception):
            """Raise this exception to mark a test as skipped.
            """
            pass


class Selenium(Plugin):
    name = 'selenium'
    loader = None

    def options(self, parser, env=os.environ):
        super(Selenium, self).options(parser, env=env)
        parser.add_option('--selenium-config',
                          default=env.get('SELENIUM_CONFIG', 'selenium.json'),
                          metavar='selenium.json',
                          help='Path to selenium config file to defile '
                               'envs to run tests on. (local, grid, selenium, '
                               'capabilities, ...)')
        parser.add_option('--selenium-skip',
                          action='store_true',
                          default=env.get('SELENIUM_SKIP', False),
                          help='Skip selenium tests')

    def configure(self, options, conf):
        super(Selenium, self).configure(options, conf)
        if not self.enabled:
            return
        self.config_file = options.selenium_config
        self.skip = options.selenium_skip
        self.drivers = [Driver('firefox'), Driver('chrome')]

    def prepareTestLoader(self, loader):
        """Capture loader
        """
        old_loadTestsFromTestCase = loader.loadTestsFromTestCase

        def loadTestsFromTestCase(testCaseClass):
            loaded_suite = []
            if not issubclass(testCaseClass, SeleniumTestCase):
                loaded_suite = old_loadTestsFromTestCase(testCaseClass)
            else:
                if self.skip:
                    testCaseClass = SkipTest
                test_case_names = loader.getTestCaseNames(testCaseClass)
                if not test_case_names and hasattr(testCaseClass, 'runTest'):
                    test_case_names = ['runTest']
                for driver in self.drivers:

                    class A(testCaseClass):
                        pass

                    new_class = A
                    new_class.driver = driver
                    new_class.__name__ = "%s_sp_%s" % (driver.name,
                                                       testCaseClass.__name__)
                    new_class.__module__ = testCaseClass.__module__
                    loaded_suite.append(loader.suiteClass(
                        map(new_class, test_case_names)))
            suites = loader.suiteClass(loaded_suite)
            return suites

        loader.loadTestsFromTestCase = loadTestsFromTestCase

    def loadTestsFromName(self, name, module=None):
        """This is needs when using multithread pluggin to re-create the
        class as generate in loadTestsFromTestCase"""
        driver = None
        prefix = None
        print os.getpid(), name, module
        if name.startswith('firefox_sp_'):
            prefix = 'firefox_sp_'
            name = name[len(prefix):]
            driver = self.drivers[0]
        if name.startswith('chrome_sp_'):
            prefix = 'chrome_sp_'
            name = name[len(prefix):]
            driver = self.drivers[1]
        if not driver or not module:
            return
        parts = name.split(".")
        class_name = parts[0]
        method_name = None
        if len(parts) >= 2:
            method_name = parts[1]
        test_case_class = getattr(module, class_name)
        assert isinstance(test_case_class, object)

        class A(test_case_class):
            pass

        new_class = A
        new_class.driver = driver
        new_class.__name__ = "%s%s" % (prefix, class_name)
        new_class.__module__ = test_case_class.__module__
        if method_name:
            yield new_class(method_name)
        else:
            loader = TestLoader()
            test_case_names = loader.getTestCaseNames(new_class)
            if not test_case_names and hasattr(new_class, 'runTest'):
                test_case_names = ['runTest']
            yield loader.suiteClass(map(new_class, test_case_names))
