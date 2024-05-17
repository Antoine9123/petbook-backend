from rest_framework import generics, mixins
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from .serializers import PostSerializer
from .permissions import OwnerOrReadOnly
from .models import Post
from follows.models import Follow


class PostListCreateView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    permission_classes = [IsAuthenticated]

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)
        return super().perform_create(serializer)

    def get(self, request:Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request:Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class PostRetrieveUpdateDeleteView(generics.GenericAPIView, 
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin, 
        mixins.DestroyModelMixin
):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    permission_classes = [OwnerOrReadOnly, IsAuthenticated]  

    def get(self, request:Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request:Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request:Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class ListPostForPet(generics.GenericAPIView,
    mixins.ListModelMixin
):
    queryset = Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        pet=self.kwargs.get("pet_id")
        return Post.objects.filter(pet=pet).order_by('-created_at')

    def get(self, request:Request, *args, **kwargs):
        return self.list(request,*args, **kwargs)
    
class ListPostForCategory(generics.GenericAPIView,
    mixins.ListModelMixin
):
    queryset = Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        category=self.kwargs.get("category")
        return Post.objects.filter(pet__gender=category).order_by('-created_at')

    def get(self, request:Request, *args, **kwargs):
        return self.list(request,*args, **kwargs)

class UserFeedListView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        followed_pets = Follow.objects.filter(owner=user).values_list('pet', flat=True)
        
        queryset = Post.objects.filter(pet__in=followed_pets).order_by('-created_at')
        
        return queryset