from rest_framework import serializers

from users.serializers import UserNoDetailSerializer

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    user = UserNoDetailSerializer(read_only=True)

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
        depth = 1
