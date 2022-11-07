import uuid

from django.db import models


class NotificationType(models.TextChoices):
    COMMENT = "comment"
    LIKE = "like"


class Notification(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.CharField(
        max_length=7,
        choices=NotificationType.choices,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_readed = models.BooleanField(default=False)

    post = models.ForeignKey(
        "posts.Post",
        on_delete=models.CASCADE,
        related_name="notifications",
    )
    owner_user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="owner_notifications",
    )
    launcher_user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="launcher_notifications",
    )
