from rest_framework import serializers
from rest_framework.reverse import reverse
from datetime import date

from .models import Pet


class PetSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    age = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Pet
        fields = [
            'id',
            'url',
            'name', 
            'gender',
            'birth',
            'age',
            'description',
            'photo_url',
            'owner_id'
        ]
    
    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("pet-detail", kwargs={"id": obj.id}, request=request)
    
    def get_age(self, obj):
        today = date.today()
        birth_date = obj.birth
        
        # Calculate age
        years = today.year - birth_date.year
        months = today.month - birth_date.month
        if today.day < birth_date.day:
            months -= 1
        if months < 0:
            years -= 1
            months += 12
        
        # Format age
        if years == 0:
            if months == 1:
                return f"{months} month"
            else:
                return f"{months} months"
        elif years == 1:
            if months == 0:
                return f"{years} year"
            elif months == 1:
                return f"{years} year and {months} month"
            else:
                return f"{years} year and {months} months"
        else:
            if months == 0:
                return f"{years} years"
            elif months == 1:
                return f"{years} years and {months} month"
            else:
                return f"{years} years and {months} months"