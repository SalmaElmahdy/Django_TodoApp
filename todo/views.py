from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Task

# Create your views here.
def add(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def done(request,pk):
    task =get_object_or_404(Task,pk=pk)
    task.is_completed=True
    task.save()
    return redirect('home')

def undo(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.is_completed=False
    task.save()
    return redirect('home')

def edit(request,pk):
    task=get_object_or_404(Task,pk=pk)
    if request.method=='POST':
        new_task=request.POST['task']
        task.task=new_task
        task.save()
        return redirect('home')
    
    context={
        'task':task,
    }
    return render(request,'edit_task.html',context)

def delete(request,pk):
     task=get_object_or_404(Task,pk=pk)
     task.delete()
     return redirect('home')