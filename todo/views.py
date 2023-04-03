from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy
from django.views import generic

from .forms import TaskForm
from .models import Task, Tag


def index(request):
    context = {}

    return render(request, "todo/index.html", context=context)


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("manager:task-list")


def pages(request):
    context = {}
    html_template = loader.get_template("todo/page-404.html")
    return HttpResponse(html_template.render(context, request))
