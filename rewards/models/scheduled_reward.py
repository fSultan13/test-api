from django.db import models

from users.models import User


class ScheduledReward(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name='scheduled_rewards'
    )
    amount = models.IntegerField(
        verbose_name="Количество монет",
        help_text="Сумма для начисления"
    )
    execute_at = models.DateTimeField(
        verbose_name="Время выполнения",
        help_text="Дата/время начисления награды"
    )
    task_id = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="ID задачи Celery",
    )

    class Meta:
        verbose_name = "Отложенная награда"
        verbose_name_plural = "Отложенные награды"
        ordering = ['-execute_at']

    def __str__(self):
        return f"{self.user.username} - {self.amount} coins at {self.execute_at}"