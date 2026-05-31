from django.shortcuts import render
from teacher.models import Teacher
from api.models import ClassRoom

def create_teacher(request):
    success_message = None
    error_message = None

    if request.method == 'POST':
        teacher_name = request.POST.get('teacher_name')
        classroom_no = request.POST.get('teacher_class')
        teacher_email = request.POST.get('teacher_email')

        try:
            classroom = ClassRoom.objects.get(class_no=classroom_no)
            Teacher.objects.create(
                teacher_name=teacher_name,
                classroom=classroom,
                teacher_email=teacher_email,
            )
            success_message = f"Assigned {teacher_name} as the teacher for {classroom}."
                
        except ClassRoom.DoesNotExist:
            error_message = "Class not found."

    classrooms = ClassRoom.objects.all().order_by('class_no')
    return render(request, 'create_teacher.html', {
        'message': success_message,
        'error': error_message,
        'classrooms': classrooms
    })