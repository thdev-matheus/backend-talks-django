from django.urls import path

from . import views

urlpatterns = [
    path(
        "notifications/",
        views.NotificationsViews.as_view(),
    ),
]
