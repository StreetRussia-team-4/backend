# Generated by Django 5.0.6 on 2024-05-21 00:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FederalManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
                ('career_start', models.DateField(verbose_name='Начало карьеры')),
                ('city_of_birth', models.CharField(max_length=255, verbose_name='Место рождения')),
                ('bio', models.TextField(verbose_name='Биография')),
                ('vk_page', models.URLField(blank=True, verbose_name='Страница Вконтакте')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('tel', models.CharField(max_length=12, verbose_name='Телефон')),
                ('photo', models.ImageField(upload_to='images/', verbose_name='Фото')),
                ('banner', models.ImageField(upload_to='images/', verbose_name='Банер')),
                ('video', models.URLField(blank=True, null=True, verbose_name='Ссылка на видео')),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='info.discipline', verbose_name='Дисциплина')),
            ],
            options={
                'verbose_name': 'Федеральный руководитель',
                'verbose_name_plural': 'Федеральное руководство',
            },
        ),
        migrations.CreateModel(
            name='RegionalManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
                ('career_start', models.DateField(verbose_name='Начало карьеры')),
                ('city_of_birth', models.CharField(max_length=255, verbose_name='Место рождения')),
                ('bio', models.TextField(verbose_name='Биография')),
                ('vk_page', models.URLField(blank=True, verbose_name='Страница Вконтакте')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('tel', models.CharField(max_length=12, verbose_name='Телефон')),
                ('photo', models.ImageField(upload_to='images/', verbose_name='Фото')),
                ('banner', models.ImageField(upload_to='images/', verbose_name='Банер')),
                ('video', models.URLField(blank=True, null=True, verbose_name='Ссылка на видео')),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='info.discipline', verbose_name='Дисциплина')),
            ],
            options={
                'verbose_name': 'Региональный руководитель',
                'verbose_name_plural': 'Региональное руководство',
                'default_related_name': 'regional_managers',
            },
        ),
    ]
