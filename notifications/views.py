from rest_framework import generics, mixins, permissions, views
from rest_framework.authentication import TokenAuthentication

from .models import Notification
from .serializers import NotificationSerializer


class NotificationsViews(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

    def get(self, request, *args, **kwargs):
        user = request.user
        notifications = self.get_queryset().filter(
            owner_user=user,
            is_readed=False,
        )
        serializer = self.get_serializer(notifications, many=True)

        response = {
            "count": notifications.count(),
            "results": serializer.data,
        }

        return views.Response(response)

    def patch(self, request, *args, **kwargs):
        user = request.user
        notifications = self.get_queryset().filter(
            owner_user=user,
            is_readed=False,
        )

        if notifications:
            for notification in notifications:
                notification.is_readed = True
                notification.save()

        return views.Response(status=views.status.HTTP_204_NO_CONTENT)
