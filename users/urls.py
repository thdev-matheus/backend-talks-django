from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path("users/", views.UsersView.as_view()),
    path("users/<str:user_id>", views.UsersDetailView.as_view()),
    # path("login/", obtain_auth_token),
    path("login/", views.UserLoginView.as_view()),
]
