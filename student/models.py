from django.db import models
from api.models import ClassRoom

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    student_email = models.EmailField(unique=True)
    classroom = models.ForeignKey(ClassRoom,on_delete=models.CASCADE,related_name="students")

    def __str__(self):
        return self.student_name