Easy Solar Challenge
==========

A microservice that takes english text and translates it into Pig Latin.
This microservice should expose an HTTP endpoint that developers can submit their strings to which will return the translation. The translation should have matching capitalization and punctuation

Prerequisites
--------

**docker** and **docker-compose**

Settings
--------
The microservice uses Docker, Docker-compose, and Flask

* Clone the project by typing::

    $ git clone https://github.com/thiernomoudou/es_challenge.git

* To create a build,  ** cd into the es_challenge directory** and type::

    $ docker-compose build


* To start the application,  excute the following::

    $ docker-compose up


The application will be available on **localhost:4000/**

To submit a phrase to translate, use the following endpoint:
**localhost:4000/translate**.

* To run tests::

    $ python3 -m unittest test.py


Clients
--------

Python client
^^^^^^^^^^^^^^

* To use the python client, execute the following ::

    $ python pyclient.py <sentence to translate>

**<sentence to translate>** should be a string (quoted if contains more than one word)


Javascript client
^^^^^^^^^^^^^^

