from django.urls import path
from .views import StudentCBVM


urlpatterns = [
    
    path('',StudentCBVM.as_view(), name="student_view")
]
