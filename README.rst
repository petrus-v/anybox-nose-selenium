

Contribute
==========


.. code-block:: bash

    nosetests anybox/nose_selenium/tests/ -v -s --log-config logging.conf

.. code-block:: bash

    nosetests examples/ -v -s --log-config logging.conf --with-selenium \
              --processes 2 --process-timeout 5
