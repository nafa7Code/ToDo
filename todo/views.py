from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user, is_completed=False).order_by('-updated_at')
    completed_tasks = Task.objects.filter(user=request.user, is_completed=True).order_by('-updated_at')
    today = datetime.now().strftime("%dth %B %Y")
    return render(request, 'todo/home.html', {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
        'today': today,
        'year': datetime.now().year
    })

@login_required
def addTask(request):
    if request.method == 'POST':
        task_text = request.POST.get('task')
        if task_text:
            Task.objects.create(
                user=request.user,
                task=task_text
            )
    return redirect('home')

@login_required
def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.is_completed = True
    task.save()
    return redirect('home')

@login_required
def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.is_completed = False
    task.save()
    return redirect('home')

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('home')

@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        new_text = request.POST.get('task')
        if new_text:
            task.task = new_text
            task.save()
        return redirect('home')
    return render(request, 'todo/edit_task.html', {'get_task': task})



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
