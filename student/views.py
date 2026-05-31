from django.shortcuts import render, get_object_or_404
from .models import Student
from api.models import ClassRoom

def create_student(request):
    success_message = None
    error_message = None

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        date_of_birth = request.POST.get('date_of_birth')
        student_email = request.POST.get('student_email')
        classroom_no = request.POST.get('ClassRoom')

        try:
            classroom = ClassRoom.objects.get(class_no=classroom_no)
            
            student = Student.objects.create(
                student_name=student_name,
                date_of_birth=date_of_birth,
                classroom=classroom,
                student_email=student_email,
            )
            success_message = f"Student {student.student_name} assigned to {classroom} successfully!"
        except ClassRoom.DoesNotExist:
            error_message = "That classroom doesn't exist yet."

    classrooms = ClassRoom.objects.all().order_by('class_no')
    return render(request, 'create_student.html', {
        'message': success_message,
        'error': error_message,
        'classrooms': classrooms
    })

def transfer_student(request):
    success_message = None
    error_message = None
    
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        new_class_no = request.POST.get('new_class_no')
        
        try:
            student = get_object_or_404(Student, id=student_id)
            new_classroom = get_object_or_404(ClassRoom, class_no=new_class_no)
            
            old_classroom = student.classroom
            student.classroom = new_classroom
            student.save()
            
            success_message = f"Transferred {student.student_name} from {old_classroom} to {new_classroom}!"
        except Exception as erroe:
            error_message = f"Transfer failed: {erroe}"

    students = Student.objects.all()
    classrooms = ClassRoom.objects.all().order_by('class_no')
    
    return render(request, 'transfer_student.html', {
        'students': students,
        'classrooms': classrooms,
        'message': success_message,
        'error': error_message
    })