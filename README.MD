# Django REST api 

Basic rest api endpoints with "Event" model for internal use.

## Description

This project template is designed to be used with [Vue client for django](https://github.com/freezerain/vue-django-client).

## Getting Started

### Dependencies

Python, Django and Django-rest-framework. Details can be found in requirements.txt

### Installing

* ```$ pip install -r requirements.txt```
* ```$ manage.py makemigrations```
* ```$ manage.py migrate```
* ```$ manage.py createsuperuser```
* ```$ manage.py runserver```

### Running

Default django rest server UI should be accessible on http://127.0.0.1:8000/

Available DB endpoints:
* user table: http://127.0.0.1:8000/users/
* events table: http://127.0.0.1:8000/events/
* groups table(internal use): http://127.0.0.1:8000/groups/
* permission table(not used): http://127.0.0.1:8000/permission/

Available server endpoints:
* Django-rest - admin cabinet: http://127.0.0.1:8000/admin/
* Django-rest - login UI: http://127.0.0.1:8000/api-auth/login/
* Django-rest - logout: http://127.0.0.1:8000/api-auth/logout/
* Django-rest - admin cabinet: http://127.0.0.1:8000/admin/
* Client - get token by username:password: http://127.0.0.1:8000/api-token-auth/
* Client - register new user: http://127.0.0.1:8000/register/

## Authors

🔥Ilia Rodikov - freeze.eli@gmail.com🔥
