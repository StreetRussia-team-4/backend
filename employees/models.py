from django.db import models

from info.models import Discipline
from media_content.models import Image, Video
from regional_offices.models import Region


class Employee(models.Model):
    description = models.TextField('Описание')
    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    birthday = models.DateField('Дата рождения')
    career_start = models.DateField('Начало карьеры')
    citi_of_birth = models.CharField('Место рождения', max_length=255)
    bio = models.TextField('Биография')
    vk_page = models.URLField('Страница Вконтакте', blank=True)
    email = models.EmailField('Электронная почта')
    tel = models.CharField('Телефон', max_length=12)
    photo = models.ForeignKey(Image,
                              verbose_name='Фото',
                              to_field='image',
                              related_name='+',
                              on_delete=models.PROTECT)
    banner = models.ForeignKey(Image,
                               verbose_name='Банер',
                               to_field='image',
                               related_name='+',
                               on_delete=models.PROTECT)
    video = models.ForeignKey(Video,
                              verbose_name='Ссылка на видео',
                              to_field='video',
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True)
    discipline = models.ForeignKey(Discipline,
                                   verbose_name='Дисциплина',
                                   on_delete=models.PROTECT)

    class Meta:
        abstract = True
        default_related_name = '+'


class FederalManager(Employee):
    class Meta:
        verbose_name = 'Федеральный руководитель'
        verbose_name_plural = 'Федеральное руководство'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class RegionalManager(Employee):
    region = models.ForeignKey(Region,
                               verbose_name='Регион',
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Региональный руководитель'
        verbose_name_plural = 'Региональное руководство'
        default_related_name = 'regional_managers'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
