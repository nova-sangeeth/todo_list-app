from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .models import todoItems
from django.utils import timezone


def todoview(request):
    all_todo_items = todoItems.objects.all()
    return render(request, 'todo.html', {'all_items': all_todo_items})


def addtodo(request):
    new_items = todoItems(content=request.POST['content'])
    new_items.save()
    return HttpResponseRedirect('/todo')


def deletetodo(request, todo_id):
    items_to_delete = todoItems.objects.get(id=todo_id)
    items_to_delete.delete()
    return HttpResponseRedirect('/todo/')
