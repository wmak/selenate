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

Browser
======
Currently selenate only supports firefox so make sure that you have the most
 recent version installed

Selenium Server
===============
Selenium requires there to be a Selenium Server running in order to interact
with a browser. This server used to be hosted at `google code`_, but has since
changed and is now hosted at `googleapis.com`_. So to download the server
navigate there, find the newest version which at the time of writing is 2.41_
and download the file known as `selenium-server-standalone-2.41.0.jar`_. Selenate
includes automatic handling of this server for you if you download this file
under the name `selenium-server.jar` and store it in the same directory as your
project files.

.. _`google code`: https://code.google.com/p/selenium/downloads/list
.. _googleapis.com: http://selenium-release.storage.googleapis.com/index.html
.. _2.41: http://selenium-release.storage.googleapis.com/index.html?path=2.41/
.. _selenium-server-standalone-2.41.0.jar: http://selenium-release.storage.googleapis.com/2.41/selenium-server-standalone-2.41.0.jar

Now normally you would have to start the selenium server with something like:

.. code-block:: bash
    
    java -jar selenium-server.jar

and you should try running this regardless to check that everything is working.
But Selenate will handle starting and stoppind this whenever you run a script,
this is done in the declaration of the Selenate object

.. code-block:: python

    browser = Selenate()

