from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def create_student(request):
    success_message = None
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        date_of_birth = request.POST.get('date_of_birth')
        student_class = request.POST.get('student_class')
        student_email = request.POST.get('student_email')

        student = Student.objects.create(
            student_name=student_name,
            date_of_birth=date_of_birth,
            student_class=student_class,
            student_email=student_email,
        )
        success_message = f"Student created successfully with ID: {student.pk}"
        return HttpResponse(request, {'message': success_message}) 
    
    return render(request, 'create_student.html')