from django.db import models
from api.models import ClassRoom

CLASS_CHOICES = (
    (1, "Class 1"),
    (2, "Class 2"),
    (3, "Class 3"),
    (4, "Class 4"),
    (5, "Class 5"),
    (6, "Class 6"),
    (7, "Class 7"),
    (8, "Class 8"),
    (9, "Class 9"),
    (10, "Class 10"),
    (11, "Class 11"),
    (12, "Class 12"),
)
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    student_email = models.EmailField(unique=True)

    classroom = models.ForeignKey(
        ClassRoom,
        on_delete=models.CASCADE,
        related_name="students"
    )

    def __str__(self):
        return self.student_name