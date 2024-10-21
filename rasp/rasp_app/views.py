from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout
from .forms import *

def index(request):
    date_range = DateRange.objects.last()
    search = str(request.GET.get('find_week')).split()
    found_week = None
    if request.method == "POST":
        Task.objects.get(pk=request.POST.get('tsk_pk')).delete()
        return redirect('index')

    if len(search) == 2:
        found_week = DateRange.objects.get(left_date=search[0], right_date=search[1])
        return redirect('rasp-detail', found_week.pk)
    tasks_by_day = {}
    for task in date_range.tasks.all():
        if task.week_day not in tasks_by_day:
            tasks_by_day[task.week_day] = []
        tasks_by_day[task.week_day].append(task)

    return render(request, 'index.html', {
        'date_range': date_range,
        'found_week': found_week,
        'tasks_by_day': tasks_by_day
    })

def rasp_detail(request, pk):
    date_range = DateRange.objects.get(pk=pk)
    search = str(request.GET.get('find_week')).split()
    found_week = None
    if request.method == "POST":
        Task.objects.get(pk=request.POST.get('tsk_pk')).delete()
        return redirect('rasp-detail', pk)
    if len(search) == 2:
        found_week = DateRange.objects.get(left_date=search[0], right_date=search[1])
        return redirect('rasp-detail', found_week.pk)
    tasks_by_day = {}
    for task in date_range.tasks.all():
        if task.week_day not in tasks_by_day:
            tasks_by_day[task.week_day] = []
        tasks_by_day[task.week_day].append(task)

    return render(request, 'rasp_detail.html', {
        'date_range': date_range,
        'found_week': found_week,
        'tasks_by_day': tasks_by_day
    })

def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'admin_login.html', {"form": form})
    

def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == "POST":
        form = UpdateTaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UpdateTaskForm(instance=task)
    return render(request, 'update_task.html', {'task': task, 'form': form})

def create_week_day(request):
    if request.method == "POST":
        form = CreateWeekdayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateWeekdayForm()
    return render(request, 'create_week_day.html', {'form': form})

def out(request):
    logout(request)
    return redirect('index')

def create_week(request):
    if request.method == "POST":
        form = CreateWeekForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateWeekForm()
    return render(request, 'create_week.html', {'form': form})

def create_task(request):
    if request.method == "POST":
        form = UpdateTaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UpdateTaskForm()
    return render(request, 'create_task.html', {'form': form})

def create_lesson(request):
    form = CreateLessonForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    else:
        form = CreateLessonForm()
    return render(request, 'create_lesson.html', {'form': form})

