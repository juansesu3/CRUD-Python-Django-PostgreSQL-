from django.urls import path
from .views import list_tasks, c

urlpatterns = [
    path('', list_tasks)
    path('new/', list_tasks)
]
