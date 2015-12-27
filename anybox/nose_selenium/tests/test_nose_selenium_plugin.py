import os
from anybox.nose_selenium.plugins.selenium import Selenium
from anybox.nose_selenium.selenium import SeleniumTestCase
from nose.plugins import PluginTester
from unittest import TestCase
# from nose.plugins.multiprocess import MultiProcess


class TestNoseSeleniumPlugin(PluginTester, TestCase):
    activate = '--with-selenium'
    plugins = [Selenium()]
    args = ['--verbose']

    def test_selenium_plugin(self):
        self.assertTrue('Ran 1 test in' in self.output)
        self.assertTrue('OK' in self.output)

    def makeSuite(self):
        class TC(SeleniumTestCase):
            def test_python_web_site(self):
                self.driver.get('https://www.python.org/')
                self.assertEquals(self.driver.title, 'Welcome to Python.org')

        return [TC('test_python_web_site')]


class TestNoseSeleniumPluginMonoProcess(PluginTester, TestCase):
    activate = '--with-selenium'
    plugins = [Selenium()]
    args = ['--verbose']
    suitepath = os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..', '..', '..', 'examples'))

    def runTest(self):
        print str(self.output)
        assert 'test_python_website (examples.test_simple_case.' \
               'firefox_sp_MyTestCase) ... ok' in self.output
        assert 'test_python_website (examples.test_simple_case.' \
               'chrome_sp_MyTestCase) ... ok' in self.output
        assert 'test_anybox_website (examples.test_simple_case.' \
               'firefox_sp_MyTestCase) ... ok' in self.output
        assert 'test_anybox_website (examples.test_simple_case.' \
               'chrome_sp_MyTestCase) ... ok' in self.output
        assert 'test_basic (examples.test_simple_case.' \
               'NormalTestCase) ... ok' in self.output
        assert 'Ran 5 tests in' in self.output

# TODO: figure out why this unit test is not working as it's working
#       when lanching it manually
# class TestNoseSeleniumPluginMultiProcesses(PluginTester, TestCase):
#     activate = '--with-selenium'
#     plugins = [Selenium(), MultiProcess()]
#     args = ['--verbose', '--processes', '2', '--process-timeout', '10']
#     suitepath = os.path.abspath(os.path.join(
#             os.path.dirname(__file__), '..', '..', '..', 'examples'))
#
#     def runTest(self):
#         print str(self.output)
#         assert 'test_python_web_site (examples.test_simple_case.' \
#                'firefox_sp_MyTestCase) ... ok' in self.output
#         assert 'test_python_web_site (examples.test_simple_case.' \
#                'chrome_sp_MyTestCase) ... ok' in self.output
#         assert 'test_anybox_web_site (examples.test_simple_case.' \
#                'firefox_sp_MyTestCase) ... ok' in self.output
#         assert 'test_anybox_web_site (examples.test_simple_case.' \
#                'chrome_sp_MyTestCase) ... ok' in self.output
#         assert 'test_basic (examples.test_simple_case.' \
#                'NormalTestCase) ... ok' in self.output
#         assert 'Ran 5 tests in' in self.output
