from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    birth = models.DateField()
    description = models.TextField(blank=True, null=True, max_length=500)
    photo_url = models.CharField(max_length=200)
    owner_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
