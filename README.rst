selenate
========

.. image:: https://pypip.in/v/selenate/badge.png
    :target: http://pypi.python.or/pypi/selenate/

.. image:: https://pypip.in/d/selenate/badge.png
    :target: http://pypi.python.or/pypi/selenate/

Web Automation made easy, built around Selenium

Setting up
==========

1. First off make sure your browser is up to date

.. image:: https://affiliates.mozilla.org/media/uploads/banners/910443de740d4343fa874c37fc536bd89998c937.png?from_affiliates
    :target: //affiliates.mozilla.org/link/banner/54231

2. Download the latest selenium server look for the latest version number directory and find a file selenium-server-standalone-x.xx.x.jar) and save it as selenium-server_.jar

.. _selenium-server: http://selenium-release.storage.googleapis.com/index.html

3. Install selenate

.. code-block:: bash

    $ pip install selenate

Documentation
=============
Documentation is available at readthedocs_

.. _readthedocs: http://selenate.readthedocs.org/en/latest/

Coding
======
Here's some basic code to start a browser and navigate a little bit

.. code-block:: python

    from selenate import Selenate
    browser = Selenate() # start your browser
    browser.get("https://github.com/wmak/selenate") # go to this url
    browser.click(".mega-octicon") # click on this css element
