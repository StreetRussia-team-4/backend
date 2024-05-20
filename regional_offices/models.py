from django.db import models

from about.models import Partner
from info.models import Discipline
from media_content.models import Image, Video


class Region(models.Model):
    """Регион."""

    name = models.CharField('Название', max_length=255, unique=True)

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return f'{self.name}'


class Citi(models.Model):
    """Город."""

    name = models.CharField('Название', max_length=255, unique=True)
    region = models.ForeignKey(Region,
                               verbose_name='Регион',
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        default_related_name = 'cities'

    def __str__(self):
        return f'{self.name}'


class Spot(models.Model):
    """Локация."""

    OPEN = 'OP'
    CLOSED = 'CL'
    TYPES = (
        (OPEN, 'Уличные локации'),
        (CLOSED, 'Крытые локации'),
    )
    name = models.CharField('Название', max_length=255, unique=True)
    spot_type = models.CharField('Тип локации', max_length=2, choices=TYPES)
    address = models.CharField('Адрес', max_length=255)
    website = models.URLField('Ссылка на сайт')
    region = models.ForeignKey(Region,
                               verbose_name='Регион',
                               on_delete=models.CASCADE)
    citi = models.ForeignKey(Citi,
                             verbose_name='Город',
                             on_delete=models.CASCADE)
    discipline = models.ManyToManyField(Discipline,
                                        verbose_name='Дисциплина')
    gallery = models.ManyToManyField(Image,
                                     verbose_name='Галерея')
    videos = models.ManyToManyField(Video,
                                    verbose_name='Ссылки на видео',
                                    blank=True)

    class Meta:
        verbose_name = 'Площадка'
        verbose_name_plural = 'Площадки'
        default_related_name = 'spots'

    def __str__(self):
        return f'{self.name}'


class Event(models.Model):
    """Событие."""

    name = models.CharField('Название', max_length=255, unique=True)
    description = models.TextField('Описание')
    date = models.DateTimeField('Дата и время')
    website = models.URLField('Ссылка на сайт')
    region = models.ForeignKey(Region,
                               verbose_name='Регион',
                               on_delete=models.CASCADE)
    employee = models.ForeignKey('employees.RegionalManager',
                                 verbose_name='Сотрудник',
                                 on_delete=models.PROTECT)
    disciplines = models.ManyToManyField(Discipline,
                                         verbose_name='Дисциплины')
    partners = models.ManyToManyField(Partner,
                                      verbose_name='Партнеры',
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
        default_related_name = 'events'

    def __str__(self):
        return f'{self.name}'
