from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1) # Associate tasks with a specific user
    task_text = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    priority = models.IntegerField(default=1)

    def __str__(self):
        return self.task_text
