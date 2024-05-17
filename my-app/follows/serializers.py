from rest_framework import serializers
from rest_framework.reverse import reverse


from .models import Follow
from pets.serializers import PetSerializer


class FollowSerializer(serializers.ModelSerializer):
    pet = PetSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = ['id', 'pet'] 

