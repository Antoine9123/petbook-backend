from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10000)
    description = models.TextField(blank=True, null=True)