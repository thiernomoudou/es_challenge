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

Testing locally
----------------
----------------

Python client
^^^^^^^^^^^^^^

* To use the python client, execute the following ::

    $ python3 pyclient.py <sentence to translate>

**<sentence to translate>** should be a string (quoted if contains more than one word)


Javascript client
^^^^^^^^^^^^^^

You need to have **NodeJs** installed before using the Javascript client.

* To use it, execute the following ::

    $ node jsclient.js <sentence to translate>

**<sentence to translate>** should be a string (quoted if contains more than one word)

Deployment
-----------

Before deploying you have to make sure that **kubectl** is installed.

* To deploy the app, you first run the following ::

    $ kubectl apply -f es-deployment.yaml

* Then, type  ::

    $ kubectl apply -f es-service.yaml


If you want to scale the application, just updat the replicas field on es-deployment.yml and
apply the changes by typing the above command


If you want to re-deploy, you need to build a new image then update the es-deployment.yml image accordinly