# 🚀 Django REST API 🚀

This is a Django REST framework backend that offers some basic features and functionality for your project. You can fork it and build on it to suit your needs.
## 📝 Description 📝

This is a bare-bones base meant to be a starting point for your development. It already includes some basic features as examples, such as:

- User authentication and registration
- Token-based authentication
- CRUD operations for users, events, groups, and permissions
- Users are able to subscribe/unsubscribe to events
- Admin interface

Before starting to work on this project, please take a look at the following files:

- [settings.py](django_rest/settings.py): This file contains the configuration settings for the project, such as the installed apps, middleware, database, etc.
- [urls.py](django_rest/settings.py): This file defines the URL patterns for the project, such as the API endpoints, the admin site, the login/logout views, etc.

## 🛠 Getting Started 🛠

### 🔧 Dependencies 🔧

You will need Python, Django, and Django REST framework to run this project. The details can be found in the requirements.txt file.

### 💻 Installing 💻

To install the project, follow these steps:

- Clone the repository or download the zip file
- Create a virtual environment and activate it
- Install the required packages with the command: ```$ pip install -r requirements.txt```
- Make the database migrations with the command: ```$ manage.py makemigrations```
- Apply the migrations with the command: ```$ manage.py migrate```
- Create a superuser account with the command: ```$ manage.py createsuperuser```
- Run the development server with the command: ```$ manage.py runserver```

### 🚀 Running 🚀

The default Django REST framework UI should be accessible on http://127.0.0.1:8000/

The available API endpoints are:

- User table: http://127.0.0.1:8000/users/
- Events table: http://127.0.0.1:8000/events/
- Groups table: http://127.0.0.1:8000/groups/
- Permission table: http://127.0.0.1:8000/permission/

The available Django views are:

- Admin site: http://127.0.0.1:8000/admin/
- Login UI: http://127.0.0.1:8000/api-auth/login/
- Logout: http://127.0.0.1:8000/api-auth/logout/
- Register new user: http://127.0.0.1:8000/register/
- Get token by username:password: http://127.0.0.1:8000/api-token-auth/

## 👥 Authors 👥

🔥 Ilia Rodikov - freeze.eli@gmail.com 🔥