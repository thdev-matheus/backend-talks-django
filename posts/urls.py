from django.urls import path

from . import views

urlpatterns = [
    path(
        "posts/",
        views.PostsView.as_view(),
    ),
    path(
        "posts/<str:post_id>/",
        views.PostsDetailView.as_view(),
    ),
    path(
        "posts/user/<str:user_id>/",
        views.PostsUserView.as_view(),
    ),
]
