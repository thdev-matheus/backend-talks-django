from rest_framework import serializers

from posts.serializers import PostNoDetailSerializer
from users.serializers import UserNoDetailSerializer

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    post = PostNoDetailSerializer(read_only=True)
    launcher_user = UserNoDetailSerializer(read_only=True)

    class Meta:
        model = Notification

        fields = [
            "id",
            "type",
            "created_at",
            "is_readed",
            "post",
            "launcher_user",
        ]

        read_only_fields = [
            "id",
            "type",
            "created_at",
            "is_readed",
            "post",
            "launcher_user",
        ]
