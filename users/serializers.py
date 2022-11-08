from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "birthdate",
            "profile_image",
            "bio",
            "is_active",
            "is_superuser",
            "date_joined",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "is_active",
            "is_superuser",
            "date_joined",
            "updated_at",
        ]

        extra_kwargs = {
            "password": {
                "write_only": True,
            },
        }

    def create(self, validated_data):
        model = self.Meta.model

        instance = model.objects.create_user(**validated_data)

        return instance


class UserNoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = [
            "id",
            "username",
            "profile_image",
        ]

        read_only_fields = [
            "id",
            "username",
            "profile_image",
        ]
