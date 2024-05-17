from django.db import models
from django.contrib.auth import get_user_model

from pets.models import Pet

User = get_user_model()


class Post(models.Model):
    description = models.TextField(max_length=500)
    photo_url = models.CharField(max_length=200)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")


    def __str__(self):
        return self.name
