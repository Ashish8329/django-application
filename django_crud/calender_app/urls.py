from django.urls import path
from .views import calendar_home

urlpatterns = [
    path('', calendar_home, name='calendar_home'),
]
