from django.db import models

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

class ClassRoom(models.Model):
    class_no = models.IntegerField(choices=CLASS_CHOICES,unique=True)

    def __str__(self):
        return f"Class {self.class_no}"