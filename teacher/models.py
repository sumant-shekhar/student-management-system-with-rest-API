from django.db import models
from api.models import ClassRoom

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=50)
    teacher_email = models.EmailField(unique=True)
    classroom = models.OneToOneField(ClassRoom,on_delete=models.CASCADE,related_name="teacher")

    def __str__(self):
        return self.teacher_name