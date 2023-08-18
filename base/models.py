from django.db import models

# Create your models here.

class Label(models.Model):
    name = models.CharField(max_length=200)
    user = models.CharField(max_length=200)