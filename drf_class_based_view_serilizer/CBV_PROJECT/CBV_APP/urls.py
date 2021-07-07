from .views import TaskCBV
from django.urls import path


urlpatterns = [
   path('', TaskCBV.as_view()),
]
