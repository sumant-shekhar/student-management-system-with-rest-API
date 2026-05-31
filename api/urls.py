from django.urls import path
from . import views


urlpatterns = [
    # Classroom
    path("classroom/", views.ClassRoomListCreateView.as_view()),
    path("classroom/<int:pk>/", views.ClassRoomDetailView.as_view()),

    # Student
    path("student/", views.StudentListCreateView.as_view()),
    path("student/<int:pk>/", views.StudentDetailView.as_view()),

    # Teacher
    path("teacher/", views.TeacherListCreateView.as_view()),
    path("teacher/<int:pk>/", views.TeacherDetailView.as_view()),
]