from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """
    use to check for authorization
    """

    def has_object_permission(self, request, view, obj):
        """
        returns True if request method is GET or obj
        id is the same with user trying to edit obj
        """

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
