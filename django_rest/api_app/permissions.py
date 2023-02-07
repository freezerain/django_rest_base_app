from rest_framework import permissions


# TODO Review external code later
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object OR admin to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions.
        return obj.owner == request.user or request.user.is_superuser
