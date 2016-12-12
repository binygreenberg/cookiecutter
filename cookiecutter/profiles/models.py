from __future__ import unicode_literals

from django.db import models

from ..users.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile_of")
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username
