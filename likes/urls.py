from django.urls import path

from . import views

urlpatterns = [
    path(
        "likes/<str:post_id>/",
        views.LikesView.as_view(),
    ),
]
