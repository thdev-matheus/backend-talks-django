import uuid

from django.db import models


class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    text = models.TextField()
    image = models.URLField()

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="posts"
    )
