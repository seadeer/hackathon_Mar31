from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class User(models.Model):
	name = models.CharField(max_length=30)
	username = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)
	password = models.CharField(max_length=60)
	name = models.CharField(max_length=30)
	created_at = models.DateTimeField(datetime.now())
	def __str__(self):
		return self.name
	class Meta:
		db_table = 'users'