from rest_framework import serializers

from posts.serializers import PostSerializer
from users.serializers import UserSerializer

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)
    owner_user = UserSerializer(read_only=True)
    launcher_user = UserSerializer(read_only=True)

    class Meta:
        model = Notification

        fields = [
            "id",
            "type",
            "created_at",
            "is_readed",
            "post",
            "owner_user",
            "launcher_user",
        ]

        read_only_fields = [
            "id",
            "type",
            "created_at",
            "is_readed",
            "post",
            "owner_user",
            "launcher_user",
        ]
