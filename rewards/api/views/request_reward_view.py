from datetime import timedelta

from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.views import APIView

from rewards.models import ScheduledReward


class RequestRewardView(APIView):
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'daily-post'

    def post(self, request):
        amount = 100
        execute_at = timezone.now() + timedelta(minutes=5)
        ScheduledReward.objects.create(user=request.user, amount=amount, execute_at=execute_at)
        return Response(
            {"detail": "Награда запланирована, она будет начислена через 5 минут"},
            status=status.HTTP_201_CREATED
        )
