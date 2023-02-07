"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from django_rest.api_app import views
from django_rest.api_app.views import PermissionViewSet, RequestTokenView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'permission', PermissionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', RequestTokenView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

