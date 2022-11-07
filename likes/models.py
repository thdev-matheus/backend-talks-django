import uuid

from django.db import models


class Like(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    post = models.ForeignKey(
        "posts.Post",
        on_delete=models.CASCADE,
        related_name="likes",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="likes",
    )
