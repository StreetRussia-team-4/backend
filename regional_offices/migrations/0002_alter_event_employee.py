# Generated by Django 5.0.6 on 2024-05-21 05:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0002_initial"),
        ("regional_offices", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="employee",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="employees.regionalmanager",
                verbose_name="Сотрудник",
            ),
        ),
    ]
