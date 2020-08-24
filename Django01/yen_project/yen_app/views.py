from django.shortcuts import render, redirect
from .form import TaskForm
from .models import Task

# Create your views here.

from django.http import HttpResponse




def index(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'yen_app/index.html', {'title': 'main page of page', 'tasks': tasks})


def about(request):
    return render(request, 'yen_app/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'incorrect form'


    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'yen_app/create.html', context)
