from django.contrib.auth.models import Permission
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

from django_rest.api_app.models import Events

DEFAULT_CHAR_LENGTH = 200


class UserSerializer(serializers.HyperlinkedModelSerializer):
    #owned_events = serializers.HyperlinkedRelatedField(view_name='events-detail', many=True, read_only=True)
    owned_events = serializers.SlugRelatedField(slug_field='title', many=True, queryset=Events.objects.all())
    #subscribed_events = serializers.HyperlinkedRelatedField(view_name='events-detail', many=True, read_only=True)
    subscribed_events = serializers.SlugRelatedField(slug_field='title', many=True, queryset=Events.objects.all())

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
    #owner = serializers.HyperlinkedRelatedField(view_name='user-detail', many=False, queryset=User.objects.all())
    owner = serializers.SlugRelatedField(slug_field='username', many=False, queryset=User.objects.all())
    subscribers = serializers.SlugRelatedField(slug_field='username', many=True, queryset=User.objects.all())
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


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=4, write_only=True)

    class Meta:
        model = User
        fields = ["username", "password"]

    def validate(self, attrs):
        user = User.objects.filter(username=attrs["username"]).exists()
        if user:
            raise ValidationError("Username already exists")
        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
