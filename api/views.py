from rest_framework import generics
from student.models import Student
from teacher.models import Teacher
from api.serializer import StudentSerializer, TeacherSerializer
from rest_framework import generics
from student.models import Student
from teacher.models import Teacher
from api.serializer import StudentSerializer, TeacherSerializer
from api.pagination import CustomPagination
from api.models import ClassRoom
from api.serializer import ClassRoomSerializer


class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_fields = ['classroom']
    pagination_class = CustomPagination

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filterset_fields = ["classroom"]
    pagination_class = CustomPagination


class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class ClassRoomListCreateView(generics.ListCreateAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer


class ClassRoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer