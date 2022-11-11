import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    profile_image = models.URLField(
        default="https://i.ibb.co/hM0XsT4/21-214439-free-high-quality-person-icon-default-profile-picture.png"
    )

    bio = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = [
        "password",
        "first_name",
        "last_name",
        "birthdate",
    ]
