import logging
from anybox.nose_selenium.selenium import SeleniumTestCase
from unittest import TestCase

log = logging.getLogger(__name__)


class MyTestCase(SeleniumTestCase):
    @classmethod
    def setUpClass(cls):
        super(MyTestCase, cls).setUpClass()
        cls.log_message("setUpClass", cls)

    def setUp(self):
        super(MyTestCase, self).setUp()
        self.sel = self.selenium
        self.log_message("setUp", self)

    def test_python_website(self):
        self.log_message("test_python_web_site", self)
        self.sel.get('https://www.python.org/')
        self.assertEquals(self.sel.title, 'Welcome to Python.org')

    def test_anybox_website(self):
        self.log_message("test_anybox_site", self)
        self.sel.get('https://anybox.fr/')
        self.assertNotEquals(self.sel.title, 'Welcome to Python.org')

    @classmethod
    def log_message(self, method, obj):
        log.debug(" driver id: %r - %s - instance %r", hex(id(obj.driver)),
                  method, obj)


class NormalTestCase(TestCase):

    def test_basic(self):
        self.assertTrue(True)
