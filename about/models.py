from django.db import models


class PartnerType(models.Model):
    name = models.CharField('Название', max_length=255, unique=True)

    class Meta:
        verbose_name = 'Тип партнерства'
        verbose_name_plural = 'Типы партнерства'

    def __str__(self):
        return f'{self.name}'


class Partner(models.Model):
    name = models.CharField('Название', max_length=255, unique=True)
    description = models.TextField('Описание')
    website = models.URLField('Ссылка на сайт')
    logo = models.ImageField('Логотип', upload_to='images/')
    type = models.ForeignKey(PartnerType,
                             verbose_name='Тип партнера',
                             on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
        default_related_name = 'partners'

    def __str__(self):
        return f'{self.name}'


class Contact(models.Model):
    email = models.EmailField('Электронная почта')
    tel = models.CharField('Телефон', max_length=12)
    actual_address = models.CharField('Фактический адрес', max_length=255)
    legal_address = models.CharField('Юридический адрес', max_length=255)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Document(models.Model):
    name = models.CharField('Название', max_length=255, unique=True)
    date = models.DateField('Дата документа')
    document = models.FileField('Документ', upload_to='documents/')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return f'{self.name}'
