from django.shortcuts import redirect, render
from todo_app.models import Todo
# Create your views here.
def listalltodos(request):
    todo = Todo.objects.all()
    return render(request,'todo/listalltodos.html',{'todo':todo})

def addtodo(request):
    if request.method == 'GET':
        return render(request,'todo/addtodo.html')
    
    elif request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Todo.objects.create(title=title,description=description)
        return redirect('listalltodos')
    
def deletetodo (request,id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('listalltodos')

def edittodo (request,id):
    todo = Todo.objects.get(id=id)
    if request.method == "GET":
        return render(request,'todo/edittodo.html',{'todo':todo})
    
    elif request.method == "POST":
        todo.title = request.POST['title']
        todo.description = request.POST['description']
        todo.save()
        return redirect('listalltodos')