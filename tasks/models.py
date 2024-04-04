from datetime import datetime

from django.db import models
from django.urls import reverse

# Create your models here.
class TaskGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateTimeField(null=True)
    taskgroup = models.ForeignKey(TaskGroup, on_delete=models.CASCADE, related_name="tasks", default="1")
    task_image = models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return '{}: due on {} unit(s)'.format(self.name, self.due_date) 
    
    def get_absolute_url(self):
        return reverse('tasks:task-detail', args=[str(self.pk)])
    
    @property
    def is_due(self):
        return datetime.now() >= self.due_date
    
    class Meta:
        ordering = ['due_date'] # order by due date ascending order '-due_date' is descending
        unique_together = ['name', 'due_date'] # don't create a duplicate task
        verbose_name = 'task'
        verbose_name_plural = 'tasks'