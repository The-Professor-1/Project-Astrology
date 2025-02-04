from django.db import models

# Create your models here.
class Users(models.Model):
    selfname = models.CharField(max_length=100)
    mothersname = models.CharField(max_length=100)
    sign = models.CharField(max_length=100)
    description = models.CharField(default='',max_length=10000)
class Message(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=500)