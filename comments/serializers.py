from rest_framework import serializers

from users.serializers import UserSerializer

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment

        fields = [
            "id",
            "text",
            "created_at",
            "updated_at",
            "user",
            "post",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "user",
            "post",
        ]
