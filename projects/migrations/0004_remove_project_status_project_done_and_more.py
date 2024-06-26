# Generated by Django 5.0.6 on 2024-05-21 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0003_alter_project_end_date_alter_project_start_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="status",
        ),
        migrations.AddField(
            model_name="project",
            name="done",
            field=models.BooleanField(default=False, verbose_name="Проект выполнен"),
        ),
        migrations.AlterField(
            model_name="project",
            name="funds_raised",
            field=models.DecimalField(
                decimal_places=2, max_digits=8, verbose_name="Объем финансирования"
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="goal",
            field=models.DecimalField(
                decimal_places=2, max_digits=8, verbose_name="Цель"
            ),
        ),
    ]
