from django.apps import AppConfig

from django_rest import api_app


class ApiAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_rest.api_app'
