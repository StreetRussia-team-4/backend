# Generated by Django 5.0.6 on 2024-05-21 00:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
        ('regional_offices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='regionalmanager',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regional_offices.region', verbose_name='Регион'),
        ),
    ]
