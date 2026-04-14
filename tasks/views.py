from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from .models import Tasks

# Create your views here.
def task_list(request):
    template = loader.get_template('task_list.html')
    tasks = Tasks.objects.all()
    context = {
        'tasks' : tasks
    }
    return HttpResponse(template.render(context,request))

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description',' ')
        Tasks.objects.create(title=title,description=description)
        return redirect('task_list')
    return render(request,'add_task.html')
    
def toggle_task(request,task_id):
    task = Tasks.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

def delete_task(request,task_id):
    Tasks.objects.get(id=task_id).delete()
    return redirect('task_list')
