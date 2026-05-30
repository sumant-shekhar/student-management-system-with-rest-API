from django.shortcuts import render
from .models import Student, Teacher

def dashboard(request):
    return render(request, 'dashboard.html')

def create_student(request):
    success_message = None
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
        success_message = f"Student created successfully with ID: {student.pk}"
        return render(request, 'student.html', {'message': success_message}) 
    
    return render(request, 'create_student.html')

def View_student(request):
    return render(request, 'View_student.html')

def Update_student(request):
    return render(request, 'Update_student.html')

def Delete_student(request):
    return render(request, 'Delete_student.html')

def create_teacher(request):
    if request.method == 'POST':
        teacher_name = request.POST.get('teacher_name')
        teacher_class = request.POST.get('teacher_class')
        teacher_email = request.POST.get('teacher_email')

        teacher = Teacher.objects.create(
            teacher_name = teacher_name,
            teacher_class = teacher_class,
            teacher_email = teacher_email,
        )
        success_message = f"Teacher created successfully with ID: {teacher.pk}"
        return render(request, 'student.html', {'message': success_message}) 
    return render(request, 'create_teacher.html')