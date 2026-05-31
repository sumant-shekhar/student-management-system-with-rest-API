from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_student),
    path('transfer/', views.transfer_student),
]