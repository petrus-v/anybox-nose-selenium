import logging
from anybox.nose_selenium.selenium import SeleniumTestCase

log = logging.getLogger(__name__)


class MyTestCase(SeleniumTestCase):
    @classmethod
    def setUpClass(cls):
        super(MyTestCase, cls).setUpClass()
        cls.log_message("setUpClass", cls)

    def setUp(self):
        super(MyTestCase, self).setUp()
        self.log_message("setUp", self)

    def test_python_web_site(self):
        self.log_message("test_python_web_site", self)
        self.driver.get('https://www.python.org/')
        self.assertEquals(self.driver.title, 'Welcome to Python.org')

    @classmethod
    def log_message(self, method, obj):
        log.info(" driver id: %r - %s - instance %r", hex(id(obj.driver)),
                 method, obj)
