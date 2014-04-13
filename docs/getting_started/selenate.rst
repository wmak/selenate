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
for one to change the location of the selenium server if they so want for
example:

.. code-block:: python

    from selenate import selenate
    browser = selenate(server="/servers/selenium.jar")

