Easy Solar Challenge
==========

A microservice that takes english text and translates it into Pig Latin.
This microservice should expose an HTTP endpoint that developers can submit their strings to which will return the translation. The translation should have matching capitalization and punctuation

Settings
--------
The microservice uses Docker, Docker-compose, and Flask

* To create a build,  use this command::

    $ docker-compose build


* To start the application,  excute the following::

    $ docker-compose build


The application will be available on localhost:4000

To submit a phrase to translate, use the following endpoint:
*localhost:4000/translate*
