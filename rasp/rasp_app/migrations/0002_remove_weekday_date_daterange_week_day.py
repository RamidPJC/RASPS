# Generated by Django 5.1.2 on 2024-10-17 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rasp_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weekday',
            name='date',
        ),
        migrations.AddField(
            model_name='daterange',
            name='week_day',
            field=models.ManyToManyField(to='rasp_app.weekday'),
        ),
    ]
