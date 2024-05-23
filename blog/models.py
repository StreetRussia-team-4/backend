from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class PostType(models.Model):
    """Тип записи."""

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, null=True, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Тип записи'
        verbose_name_plural = 'Типы записи'

    def __str__(self):
        return f'{self.name} ({self.order})'


class Post(models.Model):
    """Запись в блоге."""

    title = models.CharField('Название', max_length=255, unique=True)
    type = models.ForeignKey(
        PostType, verbose_name='Тип записи', on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User, verbose_name='Автор', on_delete=models.CASCADE
    )
    preview = models.ImageField('Изображение', upload_to='images/blog/')
    text = models.TextField('Текст')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f'{self.title} - {self.author.username} ({self.type.name})'
