from django.shortcuts import render
from teacher.models import Teacher
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