from rest_framework import permissions

#Custom permission for reference. djoser package will be used. 
# ATTENTION: Object permissions can be used only for single object returns. List objects needs to modify queryset in view.
class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to view/edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        '''
        if request.method in permissions.SAFE_METHODS:
            return True
        '''
        return obj.owner == request.user