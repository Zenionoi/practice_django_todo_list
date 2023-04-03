from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField(null=True)
    created_at = models.DateField(default=timezone.now)
    deadline = models.DateField(null=True, blank=True)
    done = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["done", "created_at"]
