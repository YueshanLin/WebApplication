from django.test import TestCase
from sio.models import Student, Course
import unittest
from django.test import Client


class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(andrew_id='001', first_name='Sean', last_name='Lin')
        Student.objects.create(andrew_id='002', first_name='Yueshan', last_name='Lin')

    def test_students_str(self):
        student1 = Student.objects.get(andrew_id='001')
        student2 = Student.objects.get(andrew_id='002')

        self.assertEqual(student1.__str__(), 'Sean Lin (001)')
        self.assertEqual(student2.__str__(), 'Yueshan Lin (002)')


class create_student_TestCase(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.post('create-student',
                                    {'andrew_id': 'yueshanl', 'first_name': 'aa', 'last_name': 'bb'})
        # response = self.client.post('create-student')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
