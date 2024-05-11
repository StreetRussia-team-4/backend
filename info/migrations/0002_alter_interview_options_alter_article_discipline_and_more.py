# Generated by Django 5.0.6 on 2024-05-11 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_alter_partner_options_alter_partner_type'),
        ('info', '0001_initial'),
        ('media_content', '0002_alter_image_options_alter_video_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interview',
            options={'verbose_name': 'Интервью', 'verbose_name_plural': 'Интервью'},
        ),
        migrations.AlterField(
            model_name='article',
            name='discipline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='info.discipline', verbose_name='Дисциплина'),
        ),
        migrations.AlterField(
            model_name='article',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='about.partner', verbose_name='Партнер'),
        ),
        migrations.AlterField(
            model_name='article',
            name='preview',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='media_content.image', to_field='image', verbose_name='Превью'),
        ),
        migrations.AlterField(
            model_name='film',
            name='discipline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='info.discipline', verbose_name='Дисциплина'),
        ),
        migrations.AlterField(
            model_name='film',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='about.partner', verbose_name='Партнер'),
        ),
        migrations.AlterField(
            model_name='film',
            name='preview',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='media_content.image', to_field='image', verbose_name='Превью'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='discipline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='info.discipline', verbose_name='Дисциплина'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='about.partner', verbose_name='Партнер'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='preview',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='media_content.image', to_field='image', verbose_name='Превью'),
        ),
        migrations.AlterField(
            model_name='news',
            name='discipline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='info.discipline', verbose_name='Дисциплина'),
        ),
        migrations.AlterField(
            model_name='news',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='about.partner', verbose_name='Партнер'),
        ),
        migrations.AlterField(
            model_name='news',
            name='preview',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='media_content.image', to_field='image', verbose_name='Превью'),
        ),
    ]
