from django.shortcuts import render, redirect
from firstapp.forms import TaskForm
from firstapp.models import TaskModel

def home(request):
    return render(request, 'base.html')

def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showtask')
    else:
        form = TaskForm()
    return render(request, 'addtask.html', {'form': form})
def edit(request,id):
    book = TaskModel.objects.get(pk = id)
    form = TaskForm(instance = book)
    if request.method=='POST':
        book= TaskForm(request.POST,instance = book)
        if book.is_valid():
            book.save()
            return redirect('showtask')
    return render(request,'addtask.html',{'form':form})
def show(request):
    tasks = TaskModel.objects.all()
    return render(request, 'showtask.html', {'tasks': tasks})
def Delete(request,id):
     book = TaskModel.objects.get(pk = id).delete()
     return redirect('showtask')

def Complete(request,id):
    book = TaskModel.objects.get(pk = id)
    book.is_completed=True
    book.save()
    tasks = TaskModel.objects.all()
    return render(request, 'completedtask.html', {'tasks': tasks})
def ccomplete(request):
    tasks = TaskModel.objects.all()
    return render(request, 'completedtask.html', {'tasks': tasks})

    
    