from rest_framework import generics, permissions

from rewards.models import RewardLog
from rewards.serializers import RewardLogSerializer


class RewardLogListView(generics.ListAPIView):
    serializer_class = RewardLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RewardLog.objects.filter(user=self.request.user).order_by('-given_at')
