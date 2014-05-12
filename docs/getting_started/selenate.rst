.. _selenate

Selenate
========

After importing selenate

.. code-block:: python

    from selenate import selenate

It's pretty easy to start a browser instance, and by doing so this will start
several things, first selenate checks if in the current directory whether there
is a `selenium-server.jar` file. If this file exists and one hasn't passed
`server=False` to selenate, then a server will start. Of course it's possible
for one to change the location of the selenium server.

So to start a Selenate with a selenium server from a seperate directory run it
as follows:

.. code-block:: python

    from selenate import selenate
    browser = selenate(server="/servers/selenium.jar")

Selenate Objects
================
A selenate object is the current browser instance and contains everything
required to automate itself.

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

classmethod *Selenate*. **find_element_by_locator** (locator)
    locator is a string in the format "type=locator" where type is one of the
    following: 'css', 'class' or 'id'. locator may also just be a css
    identifier.

