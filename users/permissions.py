from rest_framework import permissions, views

from .models import User


class AdminOwnerOrReadyOnly(permissions.BasePermission):
    def has_object_permission(
        self, request: views.Request, view: views.View, user: User
    ) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user.is_authenticated:
            return False

        return bool(request.user.is_superuser or request.user == user)


class AdminOrReadyOnly(permissions.BasePermission):
    def has_permission(self, request: views.Request, view: views.View) -> bool:
        if not request.user.is_authenticated:
            return False

        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_superuser
