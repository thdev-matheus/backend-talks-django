from rest_framework import serializers

from posts.serializers import PostSerializer
from users.serializers import UserSerializer

from .models import Like


class LikeSeializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    post = PostSerializer(read_only=True)

    class Meta:
        model = Like

        fields = [
            "id",
            "user",
            "post",
        ]

        read_only_fields = [
            "id",
            "user",
            "post",
        ]
