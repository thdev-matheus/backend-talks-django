from rest_framework import generics, permissions, views
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from .models import User
from .permissions import AdminOrReadyOnly, AdminOwnerOrReadyOnly
from .serializers import UserSerializer


class UsersView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AdminOrReadyOnly]

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UsersDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AdminOwnerOrReadyOnly]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_url_kwarg = "user_id"

    def perform_destroy(self, instance):
        instance.is_active = False

        instance.save()


class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        user_serializer = UserSerializer(user)
        token, created = Token.objects.get_or_create(user=user)
        return views.Response({"token": token.key, "user": user_serializer.data})


class UserReactivateView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_url_kwarg = "username"

    def update(self, request, *args, **kwargs):
        user = self.get_queryset().get(username=kwargs["username"])
        user.is_active = True
        user.save()

        serializer = self.get_serializer(user)
        return views.Response(serializer.data)
