from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class User(models.Model):
	name = models.CharField(max_length=30)
	def __str__(self):
		return self.name
	class Meta:
		db_table = 'users'