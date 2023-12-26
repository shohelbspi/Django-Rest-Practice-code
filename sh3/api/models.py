from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.IntegerField()
    dep = models.CharField(max_length=100)

