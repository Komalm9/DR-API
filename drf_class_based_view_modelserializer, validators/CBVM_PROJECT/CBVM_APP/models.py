from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    username = models.CharField(max_length=20)
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)

   