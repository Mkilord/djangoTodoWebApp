from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404

from .models import Task
from .forms import TaskForm

def todo_list(request):
    tasks= Task.objects.all()
    return render(request, 'todolist/todo_list.html',{'tasks':tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TaskForm()
    return render(request, 'todolist/todo_list.html',{'form':form})

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk = task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TaskForm(instanсe= task)
    return render(request, 'todolist/todo_list.html', {'form':form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    
    if request.method == 'POST':
        task.delete()
        return redirect('todo_list')
    
    return render(request, 'todolist/todo_list.html', {'tasks': Task.objects.all()})