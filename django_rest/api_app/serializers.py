from django.contrib.auth.models import Permission
from django.contrib.auth.models import User, Group
from rest_framework import serializers

from django_rest.api_app.models import Events

DEFAULT_CHAR_LENGTH = 200


class UserSerializer(serializers.HyperlinkedModelSerializer):
    owned_events = serializers.HyperlinkedRelatedField(view_name='events-detail', many=True, read_only=True)
    subscribed_events = serializers.HyperlinkedRelatedField(view_name='events-detail', many=True, read_only=True)

    class Meta:
        model = User
        fields = ['url', 'username', 'owned_events', 'subscribed_events']
        # exclude = ('password', 'last_login', 'is_superuser', 'last_name', '')
        # fields = '__all__'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        # fields = ['url', 'name']
        # exclude = ('permissions',)
        fields = '__all__'


class EventSerializer(serializers.HyperlinkedModelSerializer):
    # TODO
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', many=False, read_only=True)

    # users = serializers.HyperlinkedRelatedField(queryset=User.objects.all(), view_name='user-detail', many=True)
    class Meta:
        model = Events
        fields = '__all__'


# Magic because bugs in django
# https://github.com/encode/django-rest-framework/issues/1249#issuecomment-239977684
class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = ('url', 'name', 'codename', 'objects', 'natural_key')

