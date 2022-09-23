from django.db import models
from account.models import User
# Create your models here.


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    category = models.CharField(max_length = 100)
    due_date = models.DateField(auto_now_add=True)
    deleted = models.IntegerField(default=0, unique=False)

def __str__(self):
    return self.title