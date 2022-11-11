from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, permissions, views
from rest_framework.authentication import TokenAuthentication

from notifications.models import Notification
from posts.models import Post

from .models import Comment
from .permissions import AdminOrOwnerPermission
from .serializers import CommentSerializer


class CommentsView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    lookup_url_kwarg = "post_id"

    def create(self, request, *args, **kwargs):
        post = get_object_or_404(Post, id=kwargs["post_id"])

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, post=post)

        return views.Response(serializer.data, status=views.status.HTTP_201_CREATED)

    def perform_create(self, serializer, *args, **kwargs):
        # creation of comment
        user = self.request.user
        post = kwargs["post"]
        serializer.save(user=user, post=post)

        # creation of notification
        owner_user = post.user
        launcher_user = self.request.user
        type = "comment"

        if not owner_user == launcher_user:
            Notification.objects.create(
                type=type,
                post=post,
                owner_user=owner_user,
                launcher_user=launcher_user,
            )


class CommentsDetailView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AdminOrOwnerPermission]

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    lookup_url_kwarg = "comment_id"

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
