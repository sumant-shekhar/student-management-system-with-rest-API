from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # WEB page HTML
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),

    # Admin Login
    path('admin/', admin.site.urls),

    # API endpoint
    path('api/', include('api.urls')),
]