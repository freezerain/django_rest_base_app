from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

DEFAULT_CHAR_LENGTH = 200


class Events(models.Model):
    title = models.CharField(max_length=DEFAULT_CHAR_LENGTH, unique=True)
    description = models.CharField(max_length=DEFAULT_CHAR_LENGTH, blank=True)
    location = models.CharField(max_length=DEFAULT_CHAR_LENGTH, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    owner = models.ForeignKey(User, related_name='owned_events', on_delete=models.CASCADE)
    subscribers = models.ManyToManyField(User, related_name='subscribed_events', blank=True)

    class EventStatus(models.TextChoices):
        DRAFT = 'DRAFT', 'Draft'
        PRIVATE = 'PRIVATE', 'Private'
        PUBLIC = 'PUBLIC', 'Public'
        REMOVED = 'REMOVED', 'Removed'
        UNDEFINED = 'UNDEFINED', 'Undefined'

    status = models.CharField(max_length=16, choices=EventStatus.choices, default=EventStatus.DRAFT)

    def __str__(self):
        return f"{self.title} by {self.owner}"
