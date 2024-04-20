from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Status
from .forms import TaskForm


def tasks(request):
    template_dir = "tasks.html"
    context = {
        "tasks": Task.objects.all()
    }
    return render(request, template_dir, context=context)


def detail(request, id):
    template_dir = "detail.html"
    context = {
        "task": get_object_or_404(Task, id=id)
    }
    return render(request, template_dir, context=context)


def new_task(request):
    template_dir = "new_task.html"
    form = TaskForm(request.POST or None)
    context = {
        "form": form,
    }
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("tasks:tasks")

    return render(request, template_dir, context=context)


def change_status(request, id_task, id_status):
    task = get_object_or_404(Task, id=id_task)
    status = get_object_or_404(Status, id=id_status)
    task.status = status
    task.save()
    return redirect("tasks:detail", task.id)