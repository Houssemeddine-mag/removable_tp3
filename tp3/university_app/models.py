from django.db import models

class University(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'university'
        verbose_name_plural = 'Universities'


class Student(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'student'
