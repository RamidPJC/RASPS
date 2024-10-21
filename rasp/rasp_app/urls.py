from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('rasp/<int:pk>/', rasp_detail, name='rasp-detail'),
    path('login/', user_login, name='login'),
    path('task/<int:pk>/', update_task, name='update-task'),
    path('create-weekday/', create_week_day, name='create-weekday'),
    path('logout/', out, name='logout'),
    path('create-week/', create_week, name='create-week'),
    path('create-task/', create_task, name='create-task'),
    path('create-lesson/', create_lesson, name='create-lesson'),
]