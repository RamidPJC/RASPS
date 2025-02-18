# Generated by Django 5.1.2 on 2024-10-17 14:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateRange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left_date', models.DateField(verbose_name='%d/%m/%Y')),
                ('right_date', models.DateField(verbose_name='%d/%m/%Y')),
            ],
            options={
                'verbose_name': 'Диапазон дат',
                'verbose_name_plural': 'Диапазоны дат',
            },
        ),
        migrations.CreateModel(
            name='WeekDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_day', models.CharField(choices=[('ПН', 'Понедельник'), ('ВТ', 'Вторник'), ('СР', 'Среда'), ('ЧТ', 'Четверг'), ('ПТ', 'Пятница'), ('СБ', 'Суббота'), ('ВС', 'Воскресенье')], max_length=11)),
                ('task', models.TextField()),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='date', to='rasp_app.daterange')),
            ],
            options={
                'verbose_name': 'День недели',
                'verbose_name_plural': 'Дни недели',
            },
        ),
    ]
