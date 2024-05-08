from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Pet
from .serializers import PetSerializer


@api_view(['GET', 'POST'])
def pet_list(request):

    if request.method == 'GET':
        pet = Pet.objects.all()
        serializer = PetSerializer(pet, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
@api_view(['GET', 'PUT', 'DELETE'])
def pet_detail(request, id):

    try:
        pet = Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        data = {"error": "Pet not found"}
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
       serializer = PetSerializer(pet)
       return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PetSerializer(pet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        pet.delete()
        data = {"message": "pet successfully deleted"}
        return Response(data, status=status.HTTP_204_NO_CONTENT)