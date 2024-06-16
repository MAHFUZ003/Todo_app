from django.db import models

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=200)
    taskDescription = models.TextField(blank=True)  # Optional description field
    is_completed = models.BooleanField(default=False)
