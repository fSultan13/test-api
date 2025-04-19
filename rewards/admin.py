from django.contrib import admin
from rewards.models import ScheduledReward, RewardLog

@admin.register(ScheduledReward)
class ScheduledRewardAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'execute_at')
    list_filter = ('execute_at', 'user')
    search_fields = ('user__username', 'task_id')
    readonly_fields = ('task_id',)


@admin.register(RewardLog)
class RewardLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'given_at')
    list_filter = ('given_at', 'user')
    readonly_fields = ('given_at',)