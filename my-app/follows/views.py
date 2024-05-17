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

    def perform_create(self, serializer, pet):
        user = self.request.user
        serializer.save(owner=user, pet=pet)

    def post(self, request, *args, **kwargs):
        pet_id = request.data.get('pet_id')
        pet = get_object_or_404(Pet, id=pet_id)

        user = request.user
        already_following = Follow.objects.filter(owner=user, pet=pet).exists()
        if already_following:
            return Response(data={"error": "User is already following this pet."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, pet)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class FollowDeleteView(generics.DestroyAPIView):
    permission_classes = [OwnerOrReadOnly,IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user
        pet_id = self.request.data.get('pet_id')
        follow = get_object_or_404(Follow, owner=user, pet_id=pet_id)
        follow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
