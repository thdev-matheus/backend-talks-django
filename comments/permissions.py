from rest_framework import permissions, views

from .models import Comment


class AdminOrOwnerPermission(permissions.BasePermission):
    def has_object_permission(
        self, request: views.Request, view: views.View, obj: Comment
    ) -> bool:
        if not request.user.is_authenticated:
            return False

        return bool(request.user.is_superuser or request.user == obj.user)
