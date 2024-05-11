from django.db import models

from about.models import Partner
from media_content.models import Image, Video


class Discipline(models.Model):
    name = models.CharField('Название', max_length=255, unique=True)
    description = models.TextField('Описание')
    videos = models.ManyToManyField(Video,
                                    verbose_name='Ссылки на видео')

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'

    def __str__(self):
        return f'{self.name}'


class Blog(models.Model):
    name = models.CharField('Название', max_length=255, unique=True)
    description = models.TextField('Описание')
    pub_date = models.DateField('Дата публикации', auto_now_add=True)
    source_link = models.URLField('Ссылка на источник')
    discipline = models.ForeignKey(Discipline,
                                   verbose_name='Дисциплина',
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   blank=True)
    partner = models.ForeignKey(Partner,
                                verbose_name='Партнер',
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True)
    preview = models.ForeignKey(Image,
                                verbose_name='Превью',
                                to_field='image',
                                on_delete=models.PROTECT)

    class Meta:
        abstract = True
        default_related_name = '%(class)ss'


class Article(Blog):
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f'{self.name}'


class Interview(Blog):
    class Meta:
        verbose_name = 'Интервью'
        verbose_name_plural = 'Интервью'

    def __str__(self):
        return f'{self.name}'


class Film(Blog):
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return f'{self.name}'


class News(Blog):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return f'{self.name}'
