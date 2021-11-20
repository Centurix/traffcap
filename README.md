This repository is in early stages. There are lots of very broken RequestBin like projects out there, hopefully this will remain not-broken.

TRAFFCAP
========

Capture HTTP traffic. A Requestbin like application written in Python using FastAPI.

How to run this
===============

Frontend
--------

Right now, there are no automated builds for the front end. In order to compile the frontend, you will need to:

* cd tcspa
* npm install
* npm run build

Backend
-------

You will require poetry installed to get this running.

* poetry install
* poetry run gunicorn traffcap.server:app --workers 4 --worker-class uvicorn.workers.UvicornWorker

If everything has worked, you can visit http://localhost:8000 and you should see the home screen for Traffcap

How do I operate this thing?
============================

OK, so right now the frontend is only displaying results from a single endpoint (that probably doesn't exist). So ignore that for the time being.

The backend however has a bunch of functionality in several endpoints:

* /endpoints - POST, GET will create a new endpoint and list available endpoints
* /inbound_requests - GET will list all inbound requests made
* /r/{endpoint_code} - ALL HTTP VERBS, this will be the target endpoint for any external applications

If you look in the http folder you'll see a general.http file. This contains how to create an endpoint and then use it.

What's next?
============

A lot of functionality in the frontend for creating and managing endpoints
Notifications when request events arrive
A way of specifying the response payloads when a request comes in
Authentication of some kind

Future
======

This will eventually packaged up as a pypi package and also be made available as a docker image on docker hub.
Hopefully, this will be used in CICD stacks.
