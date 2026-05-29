from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student

def create_student(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dob = request.POST.get('dob')
        student_class = request.POST.get('student_class')
        father_name = request.POST.get('father_name')
        email = request.POST.get('email_id')

        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=dob,
            student_class=student_class,
            father_name=father_name,
            email=email
        )
        return HttpResponse(f"Student created successfully with ID: {student.pk}")
    
    return render(request, 'index.html')