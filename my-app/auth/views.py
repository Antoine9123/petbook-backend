from django.http import JsonResponse

from users.models import User

def signup(request):
    model_data =  User.objects.all()
    data = {}
    if model_data:
        data['email'] = model_data.email
        data['username'] = model_data.username
        data['password'] = model_data.password
        
    return JsonResponse(data)
