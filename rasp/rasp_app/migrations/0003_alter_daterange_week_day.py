# Generated by Django 5.1.2 on 2024-10-17 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rasp_app', '0002_remove_weekday_date_daterange_week_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daterange',
            name='week_day',
            field=models.ManyToManyField(related_name='wday', to='rasp_app.weekday'),
        ),
    ]