from rest_framework import serializers
from student.models import Student
from teacher.models import Teacher
from api.models import ClassRoom

class StudentSerializer(serializers.ModelSerializer):
    classroom_name = serializers.StringRelatedField(source="classroom", read_only=True)

    class Meta:
        model = Student
        fields = [
            "id",
            "student_name",
            "date_of_birth",
            "student_email",
            "classroom",
            "classroom_name",
        ]

class TeacherSerializer(serializers.ModelSerializer):
    classroom_name = serializers.StringRelatedField(source="classroom", read_only=True)

    class Meta:
        model = Teacher
        fields = [
            "id",
            "teacher_name",
            "teacher_email",
            "classroom",
            "classroom_name",
        ]

class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = "__all__"