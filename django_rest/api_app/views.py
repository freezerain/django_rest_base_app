# Create your views here.
import sys

from django.contrib.auth.models import User, Group, Permission
from django.db.migrations import serializer
from rest_framework import permissions, status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django_rest.api_app.models import Events
from django_rest.api_app.permissions import IsOwnerOrReadOnly
from django_rest.api_app.serializers import UserSerializer, GroupSerializer, EventSerializer, PermissionSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # TODO Any user should be able to register but not edit
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [IsOwnerOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]


class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # Save owner = User onCreate()
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

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
    API endpoint that allows permissions to be viewed or edited.
    """
    permission_classes = [permissions.IsAdminUser]
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
