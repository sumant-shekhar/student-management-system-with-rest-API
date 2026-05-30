from django.urls import path
from . import views

urlpatterns = [
    path('create_teacher', views.create_teacher),
]
