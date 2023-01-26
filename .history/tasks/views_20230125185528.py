from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def list_tasks(request):
    tasks = Task.objects.all()
    #print(tasks)
    return render(request,'list_tasks.html', {"tasks": tasks})

def create_task(request):
    task = Task(title=request.POST['title'], description=request.POST['description'])
    task.save()
    #print(request.POST['description'])
    return redirect('/tasks/')

def delete_task(request, task_id):
    task = Task.object.get(id=task_id)
    task.delete()
    
    #print(task_id)
    return redirect('/tasks/')
