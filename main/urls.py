from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('students/', include('student.urls')),
    path('teachers/', include('teacher.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]