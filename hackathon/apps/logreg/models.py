from django.db import models
from django.contrib.auth.models import User
from __future__ import unicode_literals
from datetime import datetime


class Profile(models.Model):
    user = models.ForeignKey(User)
    oauth_token=models.CharField(max_length=200)
    oauth_secret = models.CharField(max_length=200)

class User(models.Model):
	name = models.CharField(max_length=30)
	def __str__(self):
		return self.name
	class Meta:
		db_table = 'users'