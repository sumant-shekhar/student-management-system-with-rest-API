from django.urls import path
from . import views

urlpatterns = [
    path('api/students/', views.create_student, name='create_student'),
]