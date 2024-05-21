from django.db import models

from about.models import Partner
from regional_offices.models import Region


class Project(models.Model):
    """Проект."""
    CURRENT = "current"
    FUTURE = "future"
    DONE = "done"
    STATUS = (
        (CURRENT, 'Текущий'),
        (FUTURE, 'Предстоящий'),
        (DONE, "Выполненный"),
    )
    status = models.CharField(
        'Статус', max_length=8, choices=STATUS, default=FUTURE
    )
    name = models.CharField('Название', max_length=255, unique=True)
    description = models.TextField('Описание')
    region = models.ForeignKey(
        Region,
        verbose_name='Регион',
        on_delete=models.CASCADE
    )
    partners = models.ManyToManyField(
        Partner,
        verbose_name='Партнеры',
        blank=True
    )
    preview = models.ImageField('Изображение', upload_to='images/')
    start_date = models.DateTimeField('Дата и время')
    end_date = models.DateTimeField('Дата и время')
    funds_raised = models.IntegerField('Объем финансирования')
    goal = models.IntegerField('Цель')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        default_related_name = 'projects'

    def __str__(self):
        return f'{self.name}'
