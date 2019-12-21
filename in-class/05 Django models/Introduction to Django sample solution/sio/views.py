from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from sio.models import *

# Create your views here.
def home(request):
    all_student = Student.objects.all()
    return render(request, 'sio.html', {'students': all_student})

def add_student(request):
    errors = {}
    context = {}
    flag = True
    print("yes")
    if 'andrew-id' not in request.POST or not request.POST['andrew-id']:
        errors.append('You must enter the andrew-id of the student')
        flag = ~flag

    if 'first-name' not in request.POST or not request.POST['first-name']:
        errors.append('You must enter the first-name of the student')
        flag = ~flag

    if 'last-name' not in request.POST or not request.POST['last-name']:
        errors.append('You must enter the second-name of the student')
        flag = ~flag

    if flag:
        new_student = Student(AndrewID=request.POST['andrew-id'], FirstName=request.POST['first-name'], LastName=request.POST['last-name'])
        new_student.save()

    if flag:
        print(new_student.LastName)
    else:
        print("no LastName")

    all_student = Student.objects.all()
    context['students'] = all_student
    context['errors'] = errors

    return render(request, 'sio.html', context)





