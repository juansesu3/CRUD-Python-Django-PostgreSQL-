from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def list_tasks(request):
    return render(request,'list_tasks.html')

def create_task(request):
    Task(title=)
    #print(request.POST['description'])
    return redirect('/tasks/')
