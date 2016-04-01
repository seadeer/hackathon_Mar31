from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Profile(models.Model):
    user = models.ForeignKey(User)
    oauth_token=models.CharField(max_length=200)
    oauth_secret = models.CharField(max_length=200)
    def __unicode__(self):
        return unicode(self.user)