from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here.
def tasks_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})
# Retrieves all task objects from the database and renders tasklist.html
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
# Checks if method is poat and creates a tskform instance with submitted data        
    else:
        form = TaskForm()# If method is not post creates an empty taskform instance
    return render(request, 'add_task.html', {'form': form}) 

def update_task(request, pk):#Retrieves task with given primary key, if not found raises 404 error
    task = get_object_or_404(Task, pk=pk)       
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
 # Checks request method and creates ataskform instance with the submitted data, validates form and saves it if valid           
    else:
        form = TaskForm(instance=task)# Creates a taskform instance if method is not post
    return render(request, 'update_task.html', {'form': form})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'delete_task.html', {'task': task})            
    
def error_404(request, exception):

    return render(request, '404.html')