from django.db import models

from users.models import User


class RewardLog(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name='reward_logs'
    )
    amount = models.IntegerField(
        verbose_name="Количество монет",
        help_text="Начисленная сумма"
    )
    given_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время начисления"
    )

    class Meta:
        verbose_name = "Лог наград"
        verbose_name_plural = "Логи наград"
        ordering = ['-given_at']

    def __str__(self):
        return f"{self.user.username} +{self.amount} at {self.given_at}"