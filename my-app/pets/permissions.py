from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        print("Go to permission ---------------------------------------------------->")
        print(request.method)
        if request.method == 'GET':
            return True
        print("---PERMISSION--------------------------------------------------")
        print('obj.owner_id : ' + obj.owner_id)
        print('request.user : ' + request.user)
        return obj.owner_id == request.user.id