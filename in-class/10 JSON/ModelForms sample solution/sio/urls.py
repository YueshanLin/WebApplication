from django.urls import path
from sio.views import *

urlpatterns = [
    path('', home),
    path('home', home),  
    path('create-student', create_student),
    path('create-course', create_course),
    path('register-student', register_student),
    path('get-sample-students', get_sample_students),
    path('get-all-courses', get_all_courses),
]
