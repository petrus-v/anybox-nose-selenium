"""
Your test case class should inherit this helper class to get an instance
of driver.

If you define more than one capabilities, each classes will be duplicate
and run over different capabilities.

Those classes will be launched at the same time in different process

.. code-block::

    from anybox.nose_selenium.selenium import SeleniumTestCase


    class MyTestCase(SeleniumTestCase):

        def test_python_web_site(self):
            self.driver.get('https://www.python.org/')
            self.assertEquals(driver.title, 'Welcome to Python.org')
"""
import unittest
from selenium_extra.driver import Driver


class SeleniumTestCase(unittest.TestCase):
    driver = Driver('fake driver')
    """
    Driver will be instantiate by this plugin and available before the
    setUpClass
    """
