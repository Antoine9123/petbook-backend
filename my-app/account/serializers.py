from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import ValidationError
from.models import User


class SignupSerializer(serializers.ModelSerializer):
    email=serializers.CharField(max_length=80)
    username=serializers.CharField(max_length=45)
    password=serializers.CharField(min_length=8, write_only=True)
    class Meta(object):
        model = User
        fields = ["email", "username", "password"]

    def validate(self, attrs):
        email_exist=User.objects.filter(email=attrs['email']).exists()

        if email_exist:
            raise ValidationError("Email has already been used")
        
        return super().validate(attrs)
