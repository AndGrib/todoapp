from django.shortcuts import render,redirect
from .models import Todolist
from .forms import TodoListForm
from django.views.decorators.http import require_POST
from datetime import date

# Create your views here.

def index(request):
    show = request.GET.get('show', 'all')
    if show == 'active':
        todo_items = Todolist.objects.filter(completed=False).order_by('id')
    elif show == 'done':
        todo_items = Todolist.objects.filter(completed=True).order_by('id')
    else:
        todo_items = Todolist.objects.order_by('id')

    today = date.today().strftime('%A, %d %B')
    form = TodoListForm()
    total = Todolist.objects.count()
    done = Todolist.objects.filter(completed=True).count()
    percent = round(done / total * 100) if total else 0
    show = request.GET.get('show', 'all')
    context = {'todo_items': todo_items, 'form': form,
           'total': total, 'done': done, 'percent': percent, 'today': today, 'show': show}
    return render(request, 'todolist/index.html', context)

@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)

    if form.is_valid():
        new_todo = Todolist(text=request.POST['text'])
        new_todo.save()

    return redirect('index')

def completedTodo(request, todo_id):
    todo = Todolist.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    Todolist.objects.filter(completed__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    Todolist.objects.all().delete()

    return redirect('index')

@require_POST
def deleteSelected(request, todo_id):
    todo = Todolist.objects.get(pk=todo_id)
    todo.delete()
    return redirect('index')