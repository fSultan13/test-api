from rest_framework import serializers

from rewards.models import RewardLog


class RewardLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardLog
        fields = ['id', 'amount', 'given_at']
