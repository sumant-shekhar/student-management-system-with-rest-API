from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard , name='dashboard'),
    path('create_student', views.create_student, name='create_student'),
    path('view_student', views.View_student, name='view_student'),
    path('update_student', views.Update_student, name='update_student'),
    path('delete_student', views.Delete_student, name='delete_student'),
]