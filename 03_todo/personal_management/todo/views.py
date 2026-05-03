from django.shortcuts import render
from .models import Todo

# Create your views here.
def homepage(request):
    return render(request, 'todo/homepage.html')

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

