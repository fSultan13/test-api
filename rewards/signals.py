from django.db.models.signals import post_save
from django.dispatch import receiver

from rewards.models import ScheduledReward
from rewards.tasks import process_scheduled_reward


@receiver(post_save, sender=ScheduledReward)
def schedule_reward_task(sender, instance, created, **kwargs):
    if created:
        process_scheduled_reward.apply_async((instance.id,), eta=instance.execute_at)
