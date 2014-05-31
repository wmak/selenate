Installation
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
=======
Currently selenate only supports firefox so please ensure that you have the most
recent version of the browser installed.

Selenium Server
===============
Selenium requires there to be a Selenium Server running in order to interact
with a browser. The server used to be hosted at `google code`_, but has 
since changed and is now found at `googleapis.com`_. So to download the server
navigate there, find the newest version which at the time of writing is 2.41_
and download the file known as `selenium-server-standalone-2.41.0.jar`_. 
Selenate includes automatic management of this server for you if you download 
this file under the name `selenium-server.jar` and store it in the same 
directory as your project files.

.. _`google code`: https://code.google.com/p/selenium/downloads/list
.. _googleapis.com: http://selenium-release.storage.googleapis.com/index.html
.. _2.41: http://selenium-release.storage.googleapis.com/index.html?path=2.41/
.. _selenium-server-standalone-2.41.0.jar: http://selenium-release.storage.googleapis.com/2.41/selenium-server-standalone-2.41.0.jar

Now normally you would have to start the selenium server with something like:

.. code-block:: bash
    
    java -jar selenium-server.jar

and you should try running this regardless to check that everything is working.
Though for future runs Selenate will handle starting and stoppind this whenever 
you run a script, this is done in the declaration of the Selenate object

.. code-block:: python

    browser = Selenate()

Selenate
========

It's very easy to start a browser instance.
First import selenate:

.. code-block:: python

    from selenate import selenate

Then start your browser:

.. code-block:: python

    browser = selenate()

In the background Selenate will check whether or not you have a selenium server
running, and start one if you haven't. Then it will create a fresh session of
firefox.

Selenate Objects
================
A selenate object is the current browser instance and contains everything
required to begin automation.

Constructor:

class **Selenate**.(host, server)
    The host and server variables are assumed to be strings and neither are
    required variables..

    - the host value defaults to "127.0.0.1" and can be changed to a proxy if 
      needed.
    - The server value defaults to "./selenium-server.jar" and should be changed
      to wherever the selenium server file is located or False if this is being
      handled elsewhere

Class methods:

classmethod *Selenate*. **get** (url)
    url is a strong which is a valid url for the browser to go to.

classmethod *Selenate*. **find_element_by_locator** (locator)
    locator is a string in the format "type=locator" where type is one of the
    following: 'css', 'class' or 'id'. locator may also just be a css
    identifier. This function will return an object of the Selenate Element
    class.
    For example:

    .. code-block:: python
    
        browser = Selenate()
        browser.get("http://www.github.com/wmak/selenate")
        icon = browser.find_element_by_locator("css=.mega-octicon")
        icon = browser.find_element_by_locator(".mega-octicon")

classmethod *Selenate*. **click** (locator)
    *locator* should be formatted exactly as seen from 
    **find_element_by_locator** this will cause Selenate to click the element
    described by *locator*.

classmethod *Selenate*. **type_to** (locator, text)
    *locator* should be formatted exactly as seen from 
    **find_element_by_locator** *text* is a string. This will cause selenate to 
    enter *text* into the element described by *locator*

classmethod *Selenate*. **quit** ()
    Closes the Selenate browser, and if Selenate was in charge of the selenium
    server kills that as well.
