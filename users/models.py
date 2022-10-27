import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    email = models.EmailField(max_value=100, unique=True)
    password = models.CharField(max_value=100)

    first_name = models.CharField(max_value=50)
    last_name = models.CharField(max_value=50)
    birthdate = models.DateField()
    profile_image = models.URLField(
        default="https://i.ibb.co/hM0XsT4/21-214439-free-high-quality-person-icon-default-profile-picture.png"
    )

    bio = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)

    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = [
        "username",
        "email",
        "password",
        "first_name",
        "last_name",
        "birthdate",
    ]
