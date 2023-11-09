# Create your views here.

from django.contrib.auth.models import User, Group, Permission
from django.db.migrations import serializer
from rest_framework import permissions, status, generics
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from django_rest.api_app.models import Events
from django_rest.api_app.permissions import IsOwnerOrReadOnly
from django_rest.api_app.serializers import UserSerializer, GroupSerializer, EventSerializer, PermissionSerializer, \
    RegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint to Users data table
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint to Groups data table
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint to Events data table
    """
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, l_serializer):
        l_serializer.save(owner=self.request.user)

    @action(detail=True, methods=['post', 'get'], permission_classes=[permissions.IsAuthenticated])
    def subscribe(self, request, pk=None):
        event = self.get_object()
        user = request.user
        if user:
            event.subscribers.add(user)
            event.save()
            return Response({'status': 'Subscribed on event! :)'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post', 'get'], permission_classes=[permissions.IsAuthenticated])
    def unsubscribe(self, request, pk=None):
        event = self.get_object()
        user = request.user
        if user:
            event.subscribers.remove(user)
            event.save()
            return Response({'status': 'Unsubscribed from event! :('})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class PermissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint to Permission data table
    """
    permission_classes = [permissions.IsAdminUser]
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class RequestTokenView(ObtainAuthToken):
    """
    Requesting token for client if username and password provided
    """
    def post(self, request, *args, **kwargs):
        l_serializer = self.serializer_class(data=request.data,
                                             context={'request': request})
        l_serializer.is_valid(raise_exception=True)
        user = l_serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'is_superuser': user.is_superuser
        })


class RegisterView(generics.CreateAPIView):
    """
    Endpoint to register new user
    """
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
