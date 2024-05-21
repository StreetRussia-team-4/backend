from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    FEDERAL_MANAGER = 'FEDM'
    REGIONAL_MANAGER = 'REGM'
    USER = 'USER'
    STATUSES = (
        (FEDERAL_MANAGER, 'Федеральный руководитель'),
        (REGIONAL_MANAGER, 'Региональный руководитель'),
        (USER, 'Пользователь')
    )
    username = models.CharField('Имя пользователя', max_length=150)
    status = models.CharField('Статус', max_length=4, choices=STATUSES, default=USER)
    email = models.EmailField('Электронная почта', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
