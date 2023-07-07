from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        # return super().has_object_permission(request, view, obj)
        if request.method == 'GET' :
            return True
        if request.user == obj.user :
            return True
        else:
            return False