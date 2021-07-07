from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 50, blank = True, null = True)
    completed= models.BooleanField(default=False, blank = True, null = True)