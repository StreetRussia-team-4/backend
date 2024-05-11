from django.db import models


class Video(models.Model):
    video = models.URLField('Ссылка на видео', unique=True)

    class Meta:
        verbose_name = 'Видео'

    def __str__(self):
        return f'{self.video}'


class Image(models.Model):
    image = models.ImageField('Изображение', upload_to='images/', unique=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f'{self.image}'
