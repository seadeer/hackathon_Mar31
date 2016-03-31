from django.db import models
from datetime import datetime
from apps.logreg.models import *
# Create your models here.
class Listing(models.Model):
	lister = models.ForeignKey(User)
	address = models.CharField(max_length=100)
	description = models.CharField(max_length=200)
	bedrooms = models.IntegerField()
	rent = models.IntegerField()
	status = models.BooleanField()
	pets = models.BooleanField()
	washer = models.BooleanField()
	created_at = models.DateTimeField(datetime.now())
	def __str__(self):
		return str(self.id)
	class Meta:
		db_table = 'listings'