# Generated by Django 5.1.2 on 2024-10-17 18:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rasp_app', '0005_remove_task_date_range_alter_task_week_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_range',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='drange', to='rasp_app.daterange'),
        ),
    ]
