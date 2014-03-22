.. selenate documentation master file, created by
   sphinx-quickstart on Sun Mar 16 18:47:15 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Introduction
============
*Author* William Mak

Selenate is a python wrapper around the Selenium Python Client Driver. It's main
goal is to simplify the management of selenium server, and as well provide easy
to use functions.

Currently Selenate is in version 0.2 and has much of the preliminary ground work
complete and should be sufficiently usable, but is still missing neccesary
functionality.

Installing
==========
.. code-block:: bash

    pip install -U selenate

Example
=======
.. code-block:: python
    
    from selenate import Selenate
    browser = Selenate() # Start the selenium server, and launch firefox
    browser.get("http://www.google.com") # Load page
    browser.type_to("#gbqfq", "selenate\n") # Locate the css locator, and type
    browser.quit() # close the browser, and end the selenium server


Documentation
==================

* :ref:`test`
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

