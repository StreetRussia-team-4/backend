# Generated by Django 5.0.6 on 2024-05-11 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
        ('info', '0002_alter_interview_options_alter_article_discipline_and_more'),
        ('media_content', '0002_alter_image_options_alter_video_options'),
        ('regional_offices', '0002_alter_spot_options_alter_spot_discipline'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='regionalmanager',
            options={'default_related_name': 'regional_managers', 'verbose_name': 'Региональный руководитель', 'verbose_name_plural': 'Региональное руководство'},
        ),
        migrations.AlterField(
            model_name='federalmanager',
            name='discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='info.discipline', verbose_name='Дисциплина'),
        ),
        migrations.AlterField(
            model_name='federalmanager',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='media_content.video', to_field='video', verbose_name='Ссылка на видео'),
        ),
        migrations.AlterField(
            model_name='regionalmanager',
            name='discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='info.discipline', verbose_name='Дисциплина'),
        ),
        migrations.AlterField(
            model_name='regionalmanager',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regional_offices.region', verbose_name='Регион'),
        ),
        migrations.AlterField(
            model_name='regionalmanager',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='media_content.video', to_field='video', verbose_name='Ссылка на видео'),
        ),
    ]
