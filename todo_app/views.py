from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Todo

def index(request):
   if request.method == "POST":
      text = request.POST["text"]
      todo = Todo()
      todo.text = text
      todo.save()

  # todos = Todo.objects.all()
  #update the task
   todos = Todo.objects.filter(status=False)
   context = {
      'todos' : todos
   }
   return render(request, 'todo_app/index.html', context)

def change_status(request):
   pk = request.POST["pk"]
   todo = get_object_or_404(Todo, pk=pk)
   if "checked" in request.POST:
      todo.status = True
   else:
      todo.status = False
   todo.save()
   return HttpResponseRedirect(reverse('todo_app:index'))

def completed_todos(request):
   todos = Todo.objects.filter(status=True)
   context = {
      'todos' : todos
   }
   return render(request, 'todo_app/completed_todos.html', context)