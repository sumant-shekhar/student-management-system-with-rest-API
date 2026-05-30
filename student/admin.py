from django.contrib import admin
from student.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "student_name",
        "date_of_birth",
        "student_class",
        "student_email",
    )