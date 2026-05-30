from django.db import models

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
class Teacher(models.Model):
    teacher_name = models.CharField(max_length=50)
    teacher_class = models.IntegerField(choices=CLASS_CHOICES)
    teacher_email = models.EmailField(unique=True)

    def __str__(self):
        return self.teacher_name