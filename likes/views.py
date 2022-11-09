from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, permissions, views
from rest_framework.authentication import TokenAuthentication

from posts.models import Post

from .models import Like
from .serializers import LikeSerializer


class LikesView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    lookup_url_kwarg = "post_id"

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, id=kwargs["post_id"])
        likes = self.get_queryset()

        post_likes = likes.filter(post=post)
        page = self.paginate_queryset(post_likes)
        serializer = self.get_serializer(page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, id=kwargs["post_id"])
        likes = self.get_queryset()
        like_already_exists = likes.filter(post=post, user=request.user)

        if like_already_exists:
            res = {"detail": "Post already liked by this user"}
            return views.Response(
                res,
                views.status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.get_serializer(data={})
        serializer.is_valid()

        self.perform_create(serializer, post=post)
        return views.Response(
            serializer.data,
            status=views.status.HTTP_201_CREATED,
        )

    def perform_create(self, serializer, *args, **kwargs):
        post = kwargs["post"]
        user = self.request.user

        serializer.save(post=post, user=user)

    def delete(self, request, *args, **kwargs):
        post = get_object_or_404(Post, id=kwargs["post_id"])
        likes = self.get_queryset()
        like_exists = likes.filter(post=post, user=request.user)

        if not like_exists:
            res = {"detail": "Like not found"}
            return views.Response(
                res,
                views.status.HTTP_404_NOT_FOUND,
            )

        instance = like_exists[0]
        instance.delete()

        return views.Response(status=views.status.HTTP_204_NO_CONTENT)
