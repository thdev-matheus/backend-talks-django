from rest_framework import serializers

from users.serializers import UserNoDetailSerializer

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = UserNoDetailSerializer(read_only=True)

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

        extra_kwarg = {
            "post": {
                "write_only": True,
            }
        }
