from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Lecturer(models.Model):
    DOB = models.DateField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='lecturer_name')

    def __str__(self):
        return self.user


class Student(models.Model):
    DOB = models.DateField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class Semester(models.Model):
    year = models.IntegerField(null=False, blank=False)
    semester = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.semester + "(" + self.year + ")"


class Course(models.Model):
    code = models.CharField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)

    semester = models.ManyToManyField(Semester, null=True, blank=True)

    def __str__(self):
        return self.name


class Class(models.Model):
    numbers = models.IntegerField()
    course = models.ManyToManyField(Course, null=False, blank=False)
    semester = models.ManyToManyField(Semester, null=False, blank=False)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, null=True, blank=True)
    student = models.ManyToManyField(Student, null=True, blank=True)

    def __str__(self):
        return self.numbers


class CollegeDay(models.Model):
    date = models.DateField(null=False, blank=False)
    studyClass = models.ManyToManyField(Class, null=True, blank=True)
    student = models.ManyToManyField(Student, null=True, blank=True)
