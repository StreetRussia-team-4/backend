from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from about.models import Partner
from regional_offices.models import Region


class Project(models.Model):
    """Проект."""
    CURRENT = "current"
    FUTURE = "future"
    DONE = "done"
    STATUS = {CURRENT: 'current', FUTURE: 'future', DONE: 'done'}

    done = models.BooleanField('Проект выполнен', default=False)
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
    start_date = models.DateField('Дата начала')
    end_date = models.DateField('Дата окончания')
    funds_raised = models.DecimalField(
        'Объем финансирования', max_digits=8, decimal_places=2
    )
    goal = models.DecimalField(
        'Цель', max_digits=8, decimal_places=2
    )

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        default_related_name = 'projects'

    def __str__(self):
        return f'{self.name}'

    def clean(self):
        if (
                self.end_date and self.start_date
                and self.end_date < self.start_date
        ):
            raise ValidationError(
                {'end_date': 'Дата окончания должна быть больше даты начала'}
            )
        super().clean()

    @property
    def current_status(self):
        """Статус проекта в текущем состоянии."""
        if not self.done:
            now = timezone.now().date()
            if self.start_date <= now <= self.end_date:
                return self.STATUS[self.CURRENT]
            elif self.start_date > now:
                return self.STATUS[self.FUTURE]
        return self.STATUS[self.DONE]
