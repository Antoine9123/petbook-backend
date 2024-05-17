from rest_framework import serializers
from rest_framework.reverse import reverse


from .models import Post


class PostSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields = [
            'id',
            'url',
            'description',
            'pet',
            'owner',
            'photo_url'
        ]

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("post-detail", kwargs={"pk": obj.pk}, request=request)