from rest_framework import serializers

from users.serializers import UserNoDetailSerializer

from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    user = UserNoDetailSerializer(read_only=True)

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
