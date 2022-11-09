from django.urls import path

from . import views

urlpatterns = [
    path(
        "comments/post/<str:post_id>/",
        views.CommentsView.as_view(),
    ),
    path(
        "comments/<str:comment_id>/",
        views.CommentsDetailView.as_view(),
    ),
]
