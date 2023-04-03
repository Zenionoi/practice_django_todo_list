# Generated by Django 4.1.7 on 2023-04-03 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0002_remove_task_tag_task_tag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="tag",
            field=models.ManyToManyField(related_name="tasks", to="todo.tag"),
        ),
    ]
