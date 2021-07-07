from django.contrib import admin
from .models import Student
# Register your models here.

class StudentModelAdmin(admin.ModelAdmin):
    list_display =["id","name","email","username","password1","password2"]

admin.site.register(Student, StudentModelAdmin)