from django.db import models

# Create your models here.

class Label(models.Model):
    name = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    class Meta:
        unique_together = ('name', 'user',)


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)