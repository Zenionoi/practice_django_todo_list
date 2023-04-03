from django.contrib.admin import site
from django.contrib.auth.models import Group, User

from .models import Tag, Task

site.unregister(Group)
site.unregister(User)
site.register(Tag)
site.register(Task)
