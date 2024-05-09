from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Pet(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    birth = models.DateField()
    description = models.TextField(blank=True, null=True, max_length=500)
    photo_url = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pets")
    

    def __str__(self):
        return self.name

    