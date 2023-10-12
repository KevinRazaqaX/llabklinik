# views.py

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import Task
from .forms import TaskForm
from django.shortcuts import get_object_or_404, render
from .models import Task

def task_details(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'task_details.html', {'task': task})

def custom_logout(request):
    # Logout the user using Django's built-in logout function
    logout(request)

    # Redirect to the login page after logout
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base')  # Redirect to your home page or any desired URL after login
    return render(request, 'registration/login.html')

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('base')
@login_required
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('base')

@login_required
def base_view(request):
    tasks = Task.objects.filter(user=request.user).order_by('priority')
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Set the user for the task
            task.save()  # Save the form data to the database
            return redirect('task_list')
    return render(request, 'base.html',{'tasks': tasks,'form': form})

