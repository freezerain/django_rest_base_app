from django.db import models

# (key, title) -> enum
EVENT_STATUS = (
    ("draft", "Draft"),
    ("private", "Private"),
    ("public", "Public"),
    ("deleted", "Deleted"),
)


class Events(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=200, choices=EVENT_STATUS, default="draft")

    def __str__(self):
        return self.title + " by " + self.author
