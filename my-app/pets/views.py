from rest_framework import generics, mixins
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated


from .serializers import PetSerializer
from .permissions import OwnerOrReadOnly
from .models import Pet


class PetListCreateView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    permission_classes = [IsAuthenticated]

    serializer_class = PetSerializer
    queryset = Pet.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)
        return super().perform_create(serializer)

    def get(self, request:Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request:Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PetRetrieveUpdateDeleteView(generics.GenericAPIView, 
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin, 
        mixins.DestroyModelMixin
):
    serializer_class = PetSerializer
    queryset = Pet.objects.all()

    permission_classes = [OwnerOrReadOnly,IsAuthenticated]  

    def get(self, request:Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request:Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request:Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




class ListPetForOwner(generics.GenericAPIView,
        mixins.ListModelMixin
    ):
        queryset = Pet.objects.all()
        serializer_class=PetSerializer
        permission_classes=[IsAuthenticated]

        def get_queryset(self):
            username=self.kwargs.get("username")
            return Pet.objects.filter(owner__username=username)

        def get(self, request:Request, *args, **kwargs):
            return self.list(request,*args, **kwargs)