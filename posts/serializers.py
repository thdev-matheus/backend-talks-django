from rest_framework import serializers

from comments.serializers import CommentSerializer
from likes.serializers import LikeSerializer
from users.serializers import UserNoDetailSerializer

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    user = UserNoDetailSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "created_at",
            "updated_at",
            "text",
            "image",
            "user",
            "comments",
            "likes",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "user",
            "comments",
            "likes",
        ]


class PostNoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "text",
        ]
        read_only_fields = [
            "id",
            "text",
        ]
