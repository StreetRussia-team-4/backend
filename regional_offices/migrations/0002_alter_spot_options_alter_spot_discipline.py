# Generated by Django 5.0.6 on 2024-05-11 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_alter_interview_options_alter_article_discipline_and_more'),
        ('regional_offices', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='spot',
            options={'default_related_name': 'spots', 'verbose_name': 'Площадка', 'verbose_name_plural': 'Площадки'},
        ),
        migrations.AlterField(
            model_name='spot',
            name='discipline',
            field=models.ManyToManyField(to='info.discipline', verbose_name='Дисциплина'),
        ),
    ]