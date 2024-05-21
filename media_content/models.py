from django.db import models


class Video(models.Model):
    video = models.URLField('Ссылка на видео')

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return f'{self.video}'


class Image(models.Model):
    image = models.ImageField('Изображение', upload_to='images/')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f'{self.image}'
