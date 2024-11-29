from django.db import models


class Task(models.Model):
    content = models.TextField(max_length=512)  # -content - describes what you should do.
    date = models.DateTimeField(auto_now_add=True)  # -datetime, when a task was created
    deadline = models.DateTimeField(null=True, blank=True)  # -optional deadline datetime if a task should be done until some datetime
    is_completed = models.BooleanField()  # -the boolean field that marks if the task is done or not
    tags = models.ManyToManyField("Tag", related_name="tasks")  # -tags that are relevant for this task

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=32)  # Tag - a tag symbolizes the theme of the task and consists only of a name.

    def __str__(self):
        return self.name
