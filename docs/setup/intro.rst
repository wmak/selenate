.. _intro

Introduction
============
Selenate has dependencies on selenium, so at this point you should have
installed selenate which in turn would have installed selenium. But if you
haven't yet done that the command to install selenate is:

.. code-block:: bash

    pip install -U selenate

and if for whatever reason this doesn't install selenium as well that command
similarily follows as

.. code-block:: bash

    pip install -U selenium

Selenium Server
===============
Selenium requires there to be a Selenium Server running in order to interact
with a browser. This server used to be hosted at `google code`_, but has since
changed and is now hosted at `googleapis.com`_. So to download the server
navigate there, find the newest version which at the time of writing is 2.41_
and download the file known as `selenium-server-standalone-2.41.0.jar`. Selenate
includes automatic handling of this server for you if you download this file
under the name `selenium-server.jar` and store it in the same directory as your
project files.

.. _`google code`: https://code.google.com/p/selenium/downloads/list
.. _googleapis.com: http://selenium-release.storage.googleapis.com/index.html
.. _2.41: http://selenium-release.storage.googleapis.com/index.html?path=2.41/
.. _selenium-server-standalone-2.41.0.jar:
http://selenium-release.storage.googleapis.com/2.41/selenium-server-standalone-2.41.0.jar
