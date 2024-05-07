from django.http import JsonResponse

def signup(request):
    return JsonResponse({"message" : "everything works as expected"})
