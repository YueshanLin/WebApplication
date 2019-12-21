from django.db import models


class Student(models.Model):
    AndrewID = models.CharField(primary_key=True, max_length=200)
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)

    def __str__(self):
        return self.AndrewID + ': ' + self.FirstName + ' ' + self.LastName


class Course(models.Model):
    CourseNumber = models.CharField(primary_key=True, max_length=200)
    CourseName = models.CharField(max_length=200)
    Instructor = models.CharField(max_length=600)

    def __str__(self):
        return self.CourseNumber + ':' + self.CourseName + ' ' + self.Instructor


class Register(models.Model):
    AndrewID = models.ForeignKey(Student)
    CourseNumber = models.ForeignKey(Course)

    def __str__(self):
        return self.AndrewID + ": " + self.CourseNumber