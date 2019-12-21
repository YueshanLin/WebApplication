from django.db import models
from django.utils.timezone import make_aware
import datetime

class Student(models.Model):
    andrew_id = models.CharField(max_length=20, primary_key=True, verbose_name='Andrew ID')
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    def __unicode__(self):  # Use this for Python 2.x
        return "%s %s (%s)" % (self.first_name, self.last_name,
                               self.andrew_id)

    def __str__(self):      # Use this for Python 3.x
        return "%s %s (%s)" % (self.first_name, self.last_name,
                               self.andrew_id)


class Course(models.Model):
    course_number = models.CharField(max_length=20, primary_key=True)
    course_name = models.CharField(max_length=255)
    instructor = models.CharField(max_length=255)
    last_modified = models.DateTimeField(auto_now=True)
    students = models.ManyToManyField(Student)

    def __unicode__(self):  # Use this for Python 2.x
        return "%s: %s" % (self.course_number, self.course_name)

    def __str__(self):      # Use this for Python 3.x
        return "%s: %s" % (self.course_number, self.course_name)

    @staticmethod
    def get_changes(timestamp=0):
        t = make_aware(datetime.datetime.utcfromtimestamp(timestamp/1000.0))
        return Course.objects.filter(last_modified__gt=t).distinct()

    @property
    def html(self):
        ans = "<li id=course_%d>%s\n<oi>" % (self.course_number, escape(self.course_name))
        for student in students:
            ans += "<li id=student_%d>%s %s</li>\n" % (student.andrew_id, student.first_name, student.last_name)
        ans += "</oi></li>"
        return ans

    @staticmethod
    def get_max_time():
        return Course.objects.all().aggregate(Max('last_changed'))['last_changed__max'] or "1970-01-01T00:00+00:00"

