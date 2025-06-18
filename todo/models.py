from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    task = models.CharField(max_length=250)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
    
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # <== أضف هذا
    task = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task