from django.http import JsonResponse
from django.shortcuts import render
from django.db import transaction

from sio.forms import *
from sio.models import *


def make_view(request, messages=None, create_student_form=CreateStudentForm(), create_course_form=CreateCourseForm(),
              register_student_form=RegisterStudentForm()):
    if not messages:
        messages = []
    context = {'courses': Course.objects.all(),
               'messages': messages,
               'create_student_form': create_student_form,
               'create_course_form': create_course_form,
               'register_student_form': register_student_form,
               }
    return render(request, 'sio.html', context)


def home(request):
    return make_view(request, [])


@transaction.atomic
def create_student(request):
    form = CreateStudentForm(request.POST)
    if not form.is_valid():
        return make_view(request, create_student_form=form)

    new_student = Student(andrew_id=form.cleaned_data['andrew_id'],
                          first_name=form.cleaned_data['first_name'],
                          last_name=form.cleaned_data['last_name'])
    new_student.save()
    return make_view(request, ['Added %s' % new_student])


@transaction.atomic
def create_course(request):
    form = CreateCourseForm(request.POST)
    if not form.is_valid():
        return make_view(request, create_course_form=form)

    new_course = Course(course_number=request.POST['course_number'],
                        course_name=request.POST['course_name'],
                        instructor=request.POST['instructor'])
    new_course.save()
    return make_view(request, messages=['Added %s' % new_course])


@transaction.atomic
def register_student(request):
    form = RegisterStudentForm(request.POST)
    if not form.is_valid():
        return make_view(request, register_student_form=form)

    course = Course.objects.get(course_number=request.POST['course_number'])
    student = Student.objects.get(andrew_id=request.POST['andrew_id'])
    course.students.add(student)
    course.save()
    return make_view(request, messages=['Added %s to %s' % (student, course)])


# A short example of how to render json with a template. 
# Note the Content-type used.
def get_sample_students(request):
    paul = {'first_name': 'Paul', 'last_name': 'Aluri'}
    shannon = {'first_name': 'Shannon', 'last_name': 'Lee'}
    sample_students = [paul, shannon]
    context = {'students': sample_students}
    return render(request, 'students.json', context, content_type='application/json')


# TODO: Complete this action to generate a JSON response containing all courses
def get_all_courses(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    for course in courses:
        for student in course.students.all():
            print(student.first_name)
            print(student.last_name)

    return render(request, 'courses.json', context, content_type='application/json')
    """
    web = {'courseno': '0000', 'counseName': 'web application'}
    dataStructure = {'courseno': '0001', 'counseName': 'data structure'}
    sample_course = [web, dataStructure]
    context = {'courses': sample_course}
    return render(request, 'course.json', context, context_type='application/json')
    """


