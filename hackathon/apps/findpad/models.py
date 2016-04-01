from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Listing(models.Model):
	lister = models.ForeignKey(User)
	address = models.CharField(max_length=100)
	description = models.CharField(max_length=200)
	bedrooms = models.IntegerField()
	rent = models.IntegerField()
	isAvailable = models.BooleanField(default=True)
	pets = models.BooleanField(default=False)
	washer = models.BooleanField(default=False)
	created_at = models.DateTimeField(datetime.now())
	def __str__(self):
		return str(self.id)
	class Meta:
		db_table = 'listings'

class Message(models.Model):
	content = models.TextField(max_length=140)
	sender = models.ForeignKey(User)
	recipient = models.ForeignKey(Listing)
	created_at = models.DateTimeField(datetime.now())
	def __str__(self):
		return str(self.id)
	class Meta:
		db_table = 'messages'