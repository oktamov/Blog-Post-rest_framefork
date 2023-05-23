from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, and OPTIONS requests (read-only)
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        return obj.user == request.user
