from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} ({self.teacher})"

    class Meta:
        db_table = 'course'