from django.db import models
from django.contrib.auth import get_user_model

from pets.models import Pet

User = get_user_model()


class Follow(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follows")

    def __str__(self):
        return f"user: {self.owner} >> {self.pet}"

