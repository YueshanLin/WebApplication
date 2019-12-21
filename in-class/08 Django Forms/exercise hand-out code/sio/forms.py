from django import forms
from django.contrib.auth.models import Users

from . import models


class StudentForm(form.ModelForm):
    class Meta:
        model = models.Student
        field = ['andrew_id', 'first_name', 'last_name']

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def clean_andrew_id(self):
        andrew_id = self.cleaned_data['andrew_id']
        if models.Student.objects.filter(andrew_id=andrew_id):
            raise forms.ValidationError('Andrew ID already exists')
        return andrew_id

"""
class StudentForm(forms.Form):
    andrew_id = forms.CharField(max_length=10,
                                required=true,
                                label='Andrew ID')
    first_name = forms.CharField(max_length=200,
                                 default='',
                                 label='First Name')
    last_name = forms.CharField(max_length=200,
                                default='',
                                label='Last Name')
"""



class CourseForm(forms.Form):
    """
    course_number = forms.CharField(max_length=20,
                                    required=True,
                                    label='Course Number')
    course_name = forms.CharField(max_length=255,
                                  required=True,
                                  label='Course Name')
    instructor = forms.CharField(max_length=255,
                                 required=True,
                                 label='Instructor')
    students = forms.CharField(max_length=20,
                               label='Student')
    """
    class Meta:
        model = models.Course
        field = ['course_number', 'course_name', 'instructor', 'students']

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def clean_course_number(self):
        course_number = self.cleaned_data['course_number']
        if models.Course.objects.filter(course_number=course_number):
            raise forms.ValidationError('Course Number already exists')
        return course_number


class RegisterForm:
    class Meta:
        model = models.Register
        field = ['course_number', 'andrew_id']

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def clean_course_number(self):
        course_number = self.cleaned_data['course_number']
        if not models.Course.objects.filter(course_number=course_number):
            raise forms.ValidationError('Course number does not exist!')
        return course_number

    def cleaned_andrew_id(self):
        andrew_id = self.cleaned_data['andrew_id']
        if not models.Student.objects.filter(andrew_id=andrew_id):
            raise forms.ValidationError('Andrew ID does not exist!')
        return andrew_id


