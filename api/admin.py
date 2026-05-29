from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'admission_number',
        'first_name',
        'last_name',
        'student_class',
        'date_of_birth',
        'email',
        )

    search_fields = (
        'admission_number',
        'first_name',
        'last_name',
        'email',
        )

    list_filter = ('student_class',)