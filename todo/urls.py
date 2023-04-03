from django.urls import path
from django.urls import re_path

from .views import (
    index, pages, done_undone,
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,

)

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagListView.as_view(), name="tag-list",),
    path("tags/create/", TagCreateView.as_view(), name="tag-create",),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update",),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete",),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("cars/<int:pk>/done-undone/", done_undone, name="done-undone",),
    re_path(r"^.*$", pages, name="pages")
]

app_name = "todo"
