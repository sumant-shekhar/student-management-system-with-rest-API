from django.urls import path
from . import views

urlpatterns = [
    path('create_student', views.create_student),
]