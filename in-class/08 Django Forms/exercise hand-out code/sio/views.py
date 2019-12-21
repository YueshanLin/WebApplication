from django.shortcuts import render
from django.db import transaction

from sio.models import *

def home(request):
    context = {'courses':Course.objects.all()}
    return render(request, 'sio.html', context)

@transaction.atomic
def create_student(request):
    context = {'courses': Course.objects.all()}

    if request.method == 'GET':
        context['students'] = StudentForm()
        return render(request, 'sio.html', context)

    student = StudentForm(request.POST)
    context['students'] = student

    if not student.is_valid():
        return render(request, 'sio.html', context)

    student.save()
    """
    new_student = Student(andrew_id=student.cleaned_data['andrew_id'],
                          first_name=student.cleaned_data['first_name'],
                          last_name=student.cleaned_data['last_name'])

    new_student.save()
    """
    context['students'] = Student.objects.all()
    return render(request, 'sio.html', context)

@transaction.atomic
def create_course(request):
    context = {'students': Student.objects.all()}
    if request.method == 'GET':
        context['courses'] = CourseForm()
        return render(request, 'sio.html', context)

    course = CourseForm(request.POST)
    if not course.is_valid():
        return render(request, 'sio.html', context)

    course.save()
    """
    new_course = CourseForm(course_number=course.cleaned_data['course_number'],
                            course_name=course.cleaned_data['course_name'],
                            instructor=course.cleaned_data['instructor'])
    new_course.save()
    """
    context['courses'] = Student.objects.all()
    return render(request, 'sio.html', context)

@transaction.atomic
def register_student(request):
    context = {'registers': Register.objects.all()}
    if request.method == 'GET':
        context['registers'] = RegisterForm()
        return render(request, 'sio.html', context)

    register = RegisterForm(request.POST)
    if not register.is_valid():
        return render(request, 'sio.html', context)

    register.save()
    context['registers'] = Register.objects.all()
    return render(request, 'sio.html', context)
    """
    if not 'andrew_id' in request.POST or not request.POST['andrew_id']:
        messages.append("Andrew ID is required.")
    elif Student.objects.filter(andrew_id=request.POST['andrew_id']).count() != 1:
        messages.append("Could not find Andrew ID %s." %
                        request.POST['andrew_id'])
    if not 'course_number' in request.POST or not request.POST['course_number']:
        messages.append("Course number is required.")
    elif Course.objects.filter(course_number=request.POST['course_number']).count() != 1:
        messages.append("Could not find course %s." %
                        request.POST['course_number'])

    if messages:
        return render(request, 'sio.html', context)
    """

    """
    course = Course.objects.get(course_number=request.POST['course_number'])
    student = Student.objects.get(andrew_id=request.POST['andrew_id'])
    course.students.add(student)
    course.save()

    messages.append('Added %s to %s' % (student, course))
    return render(request, 'sio.html', context)
    """