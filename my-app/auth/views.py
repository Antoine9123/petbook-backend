import json
from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer


@api_view(["GET"])
def signup(request):
    instance =  User.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = UserSerializer(instance).data
    return Response(data, content_type='application/json')

@api_view(["POST"])
def signup(request):
    instance =  User.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = UserSerializer(instance).data
    return Response(data, content_type='application/json')
