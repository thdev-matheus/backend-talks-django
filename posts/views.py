from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, permissions, views
from rest_framework.authentication import TokenAuthentication

from users.models import User

from .models import Post
from .serializers import PostSerializer


class PostsView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostsDetailView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_url_kwarg = "post_id"

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PostsUserView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_url_kwarg = "user_id"

    def retrieve(self, request, *args, **kwargs):

        user = get_object_or_404(User, id=kwargs["user_id"])
        posts = self.get_queryset()

        user_posts = posts.filter(user=user)
        serializer = self.get_serializer(user_posts, many=True)

        return views.Response(serializer.data)
