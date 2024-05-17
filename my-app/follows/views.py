from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .permissions import OwnerOrReadOnly
from .serializers import FollowSerializer
from .models import Follow
from pets.models import Pet  

class UserFollowListView(generics.ListAPIView):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Follow.objects.filter(owner_id=user_id)

class FollowCreateView(generics.CreateAPIView):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        pet_id = self.request.data.get('pet_id')
        pet = get_object_or_404(Pet, id=pet_id)
        serializer.save(owner=self.request.user, pet=pet)

class FollowDeleteView(generics.DestroyAPIView):
    permission_classes = [OwnerOrReadOnly,IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user
        pet_id = self.request.data.get('pet_id')
        follow = get_object_or_404(Follow, owner=user, pet_id=pet_id)
        follow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
