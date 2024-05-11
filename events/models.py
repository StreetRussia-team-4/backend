from django.db import models

from about.models import Partner
from employees.models import RegionalManager
from info.models import Discipline
from media_content.models import Image, Video
from regional_offices.models import Region


class Event(models.Model):
    name = models.CharField('Название', max_length=255, unique=True)
    description = models.TextField('Описание')
    date = models.DateTimeField('Дата и время')
    website = models.URLField('Ссылка на сайт')
    region = models.ForeignKey(Region,
                               verbose_name='Регион',
                               related_name='events',
                               on_delete=models.CASCADE)
    employee = models.ForeignKey(RegionalManager,
                                 verbose_name='Сотрудник',
                                 related_name='events',
                                 on_delete=models.PROTECT)
    disciplines = models.ManyToManyField(Discipline,
                                         verbose_name='Дисциплины',
                                         related_name='events')
    partners = models.ManyToManyField(Partner,
                                      verbose_name='Партнеры',
                                      related_name='events',
                                      blank=True)
    gallery = models.ManyToManyField(Image,
                                     verbose_name='Галерея')
    video = models.ForeignKey(Video,
                              verbose_name='Ссылка на видео',
                              to_field='video',
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return f'{self.name}'
