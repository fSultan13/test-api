from celery import shared_task
from django.utils import timezone

from rewards.models import ScheduledReward, RewardLog


@shared_task
def process_scheduled_reward(reward_id):
    try:
        reward = ScheduledReward.objects.get(id=reward_id)
    except ScheduledReward.DoesNotExist:
        return
    if reward.execute_at <= timezone.now():
        user = reward.user
        user.coins += reward.amount
        user.save(update_fields=['coins'])
        RewardLog.objects.create(user=user, amount=reward.amount)
        reward.delete()
    else:
        process_scheduled_reward.apply_async((reward_id,), eta=reward.execute_at)
