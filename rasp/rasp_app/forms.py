from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import *

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите ваше имя пользователя',  
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',  
            'placeholder': 'Введите ваш пароль',
        })
    )

from django import forms
from .models import Task

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("week_day", "date_range", "lesson", "task", "file")
        widgets = {
            "week_day": forms.Select(attrs={"class": "form-control"}),
            "date_range": forms.Select(attrs={"class": "form-control"}),
            "lesson": forms.Select(attrs={"class": "form-control"}),
            "task": forms.TextInput(attrs={"class": "form-control"}),
            "file": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
        labels = {
            "week_day": "День недели",
            "date_range": "Неделя",
            "lesson": "Предмет",             
            "task": "Задание", 
            "file": "Файл",   
        }

class CreateWeekdayForm(forms.ModelForm):
    class Meta:
        model = WeekDay
        fields = ('week_day',)
        widgets = {
            "week_day": forms.Select(attrs={"class": "form-control"}),
        }
        labels = {
            "week_day": "День недели",
        }

class CreateWeekForm(forms.ModelForm):
    class Meta:
        model = DateRange
        fields = ('left_date', 'right_date', 'week_day')

        widgets = {
            'left_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                    'placeholder': 'Выберите начальную дату',
                }
            ),
            'right_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                    'placeholder': 'Выберите конечную дату',
                }
            ),
            'week_day': forms.CheckboxSelectMultiple(
                attrs={
                    'class': 'form-control',
                }
            ),
        }

        labels = {
            'left_date': 'Начальная дата',
            'right_date': 'Конечная дата',
            'week_day': 'Дни недели',
        }

class CreateLessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('title',)
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
        }

        labels = {
            "title": "Название предмета"
        }

