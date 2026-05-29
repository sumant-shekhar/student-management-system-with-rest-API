from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    student_class = models.CharField(max_length=20)
    father_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    admission_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"