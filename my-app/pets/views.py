from django.contrib.auth.models import User

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Pet
from .serializers import PetSerializer
from .permissions import IsOwnerOrReadOnly


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def pet_list(request):

    if request.method == 'GET':
        pet = Pet.objects.all()
        serializer = PetSerializer(pet, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        request.data['owner_id'] = request.user.id
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsOwnerOrReadOnly,IsAuthenticated])
def pet_detail(request, id):
    print(" going to pet detail --------------------------------------------------->")
    try:
        pet = Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        data = {"error": "Pet not found"}
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
       serializer = PetSerializer(pet)
       return Response(serializer.data)
    
    elif request.method == 'PUT':
        request.data['owner_id'] = request.user.id
        serializer = PetSerializer(data=request.data)
        serializer = PetSerializer(pet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        pet.delete()
        data = {"message": "pet successfully deleted"}
        return Response(data, status=status.HTTP_204_NO_CONTENT)