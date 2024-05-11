# Generated by Django 5.0.6 on 2024-05-11 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regional_offices', '0002_alter_spot_options_alter_spot_discipline'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='citi',
            options={'default_related_name': 'cities', 'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.AlterField(
            model_name='citi',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regional_offices.region', verbose_name='Регион'),
        ),
        migrations.AlterField(
            model_name='spot',
            name='citi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regional_offices.citi', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='spot',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regional_offices.region', verbose_name='Регион'),
        ),
    ]
