from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, pagination, permissions, views
from rest_framework.authentication import TokenAuthentication

from users.models import User

from .models import Post
from .permissions import AdminOwnerOrReadOnlyPermission
from .serializers import PostSerializer


class PostsView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostsDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AdminOwnerOrReadOnlyPermission]

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_url_kwarg = "post_id"


class PostsUserView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_url_kwarg = "user_id"

    def list(self, request, *args, **kwargs):

        user = get_object_or_404(User, id=kwargs["user_id"])
        posts = self.get_queryset()

        user_posts = posts.filter(user=user)
        page = self.paginate_queryset(user_posts)
        serializer = self.get_serializer(page, many=True)

        return self.get_paginated_response(serializer.data)
