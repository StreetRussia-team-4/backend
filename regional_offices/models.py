from django.db import models

from info.models import Discipline
from media_content.models import Image, Video


class Region(models.Model):
    name = models.CharField('Название', max_length=255, unique=True)

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return f'{self.name}'


class Citi(models.Model):
    name = models.CharField('Название', max_length=255, unique=True)
    region = models.ForeignKey(Region,
                               verbose_name='Регион',
                               related_name='cities',
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return f'{self.name}'


class Spot(models.Model):
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
                               related_name='spots',
                               on_delete=models.CASCADE)
    citi = models.ForeignKey(Citi,
                             verbose_name='Город',
                             related_name='spots',
                             on_delete=models.CASCADE)
    discipline = models.ManyToManyField(Discipline,
                                        verbose_name='Дисциплина',
                                        related_name='spots')
    gallery = models.ManyToManyField(Image,
                                     verbose_name='Галерея')
    videos = models.ManyToManyField(Video,
                                    verbose_name='Ссылки на видео',
                                    blank=True)

    class Meta:
        verbose_name = 'Площадка'
        verbose_name_plural = 'Площадки'

    def __str__(self):
        return f'{self.name}'
