from django import forms

from sio.models import *


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_number', 'course_name', 'instructor']


class RegisterStudentForm(forms.Form):
    andrew_id = forms.CharField(label='Andrew ID', max_length=20)
    course_number = forms.CharField(max_length=20)

    def clean_andrew_id(self):
        andrew_id = self.cleaned_data['andrew_id']
        andrew_id = andrew_id.lower()
        if Student.objects.filter(andrew_id=andrew_id).count() == 0:
            raise forms.ValidationError("%s is not a student" % andrew_id)
        return andrew_id

    def clean_course_number(self):
        course_number = self.cleaned_data['course_number']
        if Course.objects.filter(course_number=course_number).count() == 0:
            raise forms.ValidationError("%s is not a course" % course_number)
        return course_number
