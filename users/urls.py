from django.urls import path

from . import views

urlpatterns = [
    path(
        "users/",
        views.UsersView.as_view(),
    ),
    path(
        "users/<str:user_id>/",
        views.UsersDetailView.as_view(),
    ),
    path(
        "users/reactivate/<str:username>/",
        views.UserReactivateView.as_view(),
    ),
    path(
        "login/",
        views.UserLoginView.as_view(),
    ),
]
