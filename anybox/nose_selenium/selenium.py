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
            self.selenium.get('https://www.python.org/')
            self.assertEquals(selenium.title, 'Welcome to Python.org')
"""
import unittest


class SeleniumTestCase(unittest.TestCase):
    driver = None
    """
    Driver will be instantiate by this plugin and available before the
    setUpClass
    """
    @classmethod
    def setUpClass(cls):
        super(SeleniumTestCase, cls).setUpClass()
        # The first time we get selenium, connexion is created
        # I wonder if it's that important to do that?
        # may change in the future
        cls.selenium = cls.driver.selenium

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
