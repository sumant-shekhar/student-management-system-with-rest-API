from django.urls import path
from api import views

urlpatterns = [
    # Web page Urls
    path('student/', views.StudentListCreateAPIView.as_view()),
    path('student/<int:pk>/', views.StudentRetrieveUpdateDestroyAPIView.as_view()),
    path('teacher/', views.TeacherListCreateAPIView.as_view()),
    path('teacher/<int:pk>/', views.TeacherRetrieveUpdateDestroyAPIView.as_view()),

    # API endpoint

    
]