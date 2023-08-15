from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
def index(request):
    tasks=Task.objects.all()
    form=TaskForm()

    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        
    context={'tasks':tasks,'form':form}
    return render(request,'tasks/list.html',context)


def updateTask(request, pk):
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)

    if request.method=='POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'tasks/update_task.html',context)

def deletTask(request, pk):
     item=Task.objects.get(id=pk)
     context={'item':item}
     return render(request,'tasks/delete_task.html', context)