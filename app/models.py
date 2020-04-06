from django.db import models

# Create your models here.

class URL(models.Model):
	long_url = models.CharField(max_length=264, unique=True)
	short_url = models.CharField(max_length=264, unique=True)

