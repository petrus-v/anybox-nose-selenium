====================
Anybox-nose-selenium
====================

.. image:: https://api.travis-ci.org/petrus-v/anybox-nose-selenium.svg?branch=master
   :target: https://travis-ci.org/petrus-v/anybox-nose-selenium
   :alt: Travis

anybox-nose-selenium is a plugin for nose that provides support to launch
selenium tests, the same test case is launched over all browsers you define in
parallel.

QuickStart
==========

Your test case class should inherit SeleniumTestCase helper class to get an
instance of selenium driver (this helper class already inherit from
``unittest.TestCase``).

If you define more than one capabilities, each classes will be duplicate
and run over different capabilities.

Those classes will be launched at the same time in different process

.. code-block::

    from anybox.nose_selenium.selenium import SeleniumTestCase


    class MyTestCase(SeleniumTestCase):

        def test_python_web_site(self):
            self.selenium.get('https://www.python.org/')
            self.assertEquals(selenium.title, 'Welcome to Python.org')


To run it that

.. code-block::

    nosettests -v -s --with-selenium --selenium-config selenium.json \
                --processes 2 --process-timeout 5 test_selenium.py


where ``selenium.json`` looks like

.. code-block::

    {
      "drivers": [
        {
          "class": "selenium_extra.drivers.local.Chrome"
        },
        {
          "class": "selenium_extra.drivers.local.Firefox"
        },
        {
          "class": "selenium_extra.drivers.remote.Grid",
          "capabilities": {
              "command_executor": 'http://127.0.0.1:4444/wd/hub'
          },
          "request_drivers": [
            {
              "browserName": "firefox",
              "platform": "LINUX",
              "version": "",
              "capabilities": {
              }
            },
            {
              "browserName": "chrome",
              "platform": "LINUX",
              "version": "",
              "capabilities": {
              }
            }
          ]
        }
      ],
      "global_capabilities": {
      }
    }

Your tests will run on your local chrome and firefox browser and on a local
grid wich should contains nodes with chrome and firefox on linux machine.

Contribute
==========

You require chrome webdriver, firefox webdriver and a grid to run it locally

Setup local webdriver
---------------------

* **chrome**: https://sites.google.com/a/chromium.org/chromedriver/
* **firefox**: https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette/WebDriver


Setup grid and nodes
--------------------

https://hub.docker.com/r/selenium/
https://github.com/SeleniumHQ/docker-selenium


Run tests
---------

.. code-block:: bash

    nosetests anybox/nose_selenium/tests/ -v -s --log-config logging.conf

.. code-block:: bash

    nosetests examples/ -v -s --log-config logging.conf --with-selenium \
              --processes 2 --process-timeout 5


State
=====

In development:
* The name of this package may change.
* no compatibility warranty over versions
* The license may change to an other OSI-approved licenses
* I may squash some commit until the first release
* Main repo can move somewhere else


Know issues
===========

* It looks like setupClass is called Twice in multiprocess
* There is something wrong unittesting selenium nose pluggin in multiprocess