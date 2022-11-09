from rest_framework import permissions, views

from .models import Post


class AdminOwnerOrReadOnlyPermission(permissions.BasePermission):
    def has_object_permission(
        self, request: views.Request, view: views.View, obj: Post
    ) -> bool:
        if not request.user.is_authenticated:
            return False

        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user.is_superuser or request.user == obj.user)
