from django.db import models

class DateRange(models.Model):
    left_date = models.DateField('%d/%m/%Y', db_index=True)
    right_date = models.DateField('%d/%m/%Y', db_index=True)
    week_day = models.ManyToManyField('WeekDay', related_name='dateranges')

    class Meta:
        verbose_name = "Диапазон дат"
        verbose_name_plural = "Диапазоны дат"
    def __str__(self):
        return f'{self.left_date} - {self.right_date}'

class WeekDay(models.Model):
    week_day = models.CharField(choices=[('ПН', 'Понедельник'), ('ВТ', 'Вторник'), ('СР', 'Среда'), ('ЧТ', 'Четверг'), ('ПТ', 'Пятница'), ('СБ', 'Суббота'), ('ВС', 'Воскресенье')], max_length=11)

    class Meta:
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'
    def __str__(self):
        return self.week_day

class Lesson(models.Model):
    title = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
    def __str__(self):
        return self.title

class Task(models.Model):
    week_day = models.ForeignKey('WeekDay', related_name='tasks', on_delete=models.CASCADE)
    date_range = models.ForeignKey('DateRange', related_name='tasks', on_delete=models.CASCADE, default=DateRange.objects.last().pk)
    lesson = models.ForeignKey('Lesson', related_name='tasks', on_delete=models.CASCADE)
    task = models.TextField(blank=True)
    file = models.FileField(blank=True, null=True)
    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        ordering = ['week_day']
    def __str__(self):
        return self.task[:18]