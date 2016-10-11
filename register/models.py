from __future__ import unicode_literals
import uuid
from django.db import models
# Create your models here.
class Person(models.Model):
	def __str__(self):
		return self.name+"  "+str(self.identity)
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=50)
	roll_no=models.CharField(max_length=50)
	profession=models.CharField(max_length=50)
	college=models.TextField()
	identity = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
