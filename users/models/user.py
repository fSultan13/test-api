from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    coins = models.IntegerField(default=0, verbose_name="Монеты")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"