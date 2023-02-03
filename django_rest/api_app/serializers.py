from django.contrib.auth.models import User, Group
from rest_framework import serializers

from django_rest.api_app.models import Events, EVENT_STATUS


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class EventSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200, required=True)
    description = serializers.CharField(max_length=200, required=True)
    author = serializers.CharField(max_length=200, required=True)
    date = serializers.CharField(max_length=200, required=True)
    location = serializers.CharField(max_length=200, required=True)
    status = serializers.ChoiceField(choices=EVENT_STATUS)

    class Meta:
        model = Events
        fields = ('__all__')