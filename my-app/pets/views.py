from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, generics, mixins
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from .models import Pet
from .serializers import PetSerializer


class PetListCreateView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    permission_classes = [IsAuthenticated]

    serializer_class = PetSerializer
    queryset = Pet.objects.all()

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

    permission_classes = [IsAuthenticated]  

    def get(self, request:Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request:Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request:Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

