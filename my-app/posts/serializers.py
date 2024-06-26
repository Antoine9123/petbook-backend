from rest_framework import serializers
from rest_framework.reverse import reverse


from .models import Post


class PostSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields = [
            'id',
            'created_at',
            'url',
            'description',
            'pet',
            'photo_url'
        ]

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse("post-detail", kwargs={"pk": obj.pk}, request=request)