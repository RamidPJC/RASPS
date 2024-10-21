# Generated by Django 5.1.2 on 2024-10-17 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rasp_app', '0003_alter_daterange_week_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
            },
        ),
        migrations.RemoveField(
            model_name='weekday',
            name='task',
        ),
        migrations.AlterField(
            model_name='daterange',
            name='week_day',
            field=models.ManyToManyField(related_name='dwday', to='rasp_app.weekday'),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField()),
                ('date_range', models.ManyToManyField(related_name='drange', to='rasp_app.daterange')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lson', to='rasp_app.lesson')),
                ('week_day', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='twday', to='rasp_app.weekday')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
            },
        ),
    ]
