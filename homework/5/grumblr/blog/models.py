from django.db import models
from django.contrib.auth.models import User

from django.db.models import Max
import datetime
import time


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=42)
    #last_change = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + ' ' + self.comment

    @staticmethod
    def get_changes(time="1970-01-01 00:00"):
        return Post.objects.filter(time__gt=time).distinct()

    @property
    def html(self):
        return "" \
               "<li>\
                   <div class=\"comment_img\">\
                       <a href = \"profile/%s\"> <img src=\"photo/%s\" class =\"profile_img\" alt=\"Profile\"> </a>\
                       <a href = \"profile/%s\"> %s</a>\
                   </div>\
                   <div class =\"comment_txt\">\
                       %s  <span class =\"time\"> %s </span>\
                       <a href = \"follow/%s\"> <button> Follow </button> </a> <a href=\"unfollow/%s\"> <button> Unfollow </button> </a>\
                       <ul id=\"subPost_%s\"></ul>\
                       <ul>\
                           <li>\
                               <input type = \"text\" id=\"writeSubPost_%s\">\
                               <button id=\"submit_%s\">Submit</button>\
                           </li>\
                       </ul>\
                   </div>\
               </li>" % (self.user.id, self.user.id, self.user.id, self.user.username, self.comment, self.time, self.user.id, self.user.id, self.id, self.id, self.id)


    @staticmethod
    def get_max_time():
        # Change the date format to string type
        if Post.objects.all().aggregate(Max('time'))['time__max']:
            return Post.objects.all().aggregate(Max('time'))['time__max'].strftime("%Y-%m-%d %H:%M:%S")
        else:
            return datetime.datetime.utcfromtimestamp(0).strftime('%Y-%m-%d %H:%M:%S')


class SubPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=42)
    post = models.ForeignKey(Post, on_delete=True)

    def __str__(self):
        return self.comment + " " + self.user.username + " " + post.comment

    @staticmethod
    def get_changes(time="1970-01-01 00:00"):
        return SubPost.objects.filter(time__gt=time).distinct()

    @staticmethod
    def get_max_time():
        # Change the date format to string type
        if SubPost.objects.all().aggregate(Max('time'))['time__max']:
            return SubPost.objects.all().aggregate(Max('time'))['time__max'].strftime("%Y-%m-%d %H:%M:%S")
        else:
            return datetime.datetime.utcfromtimestamp(0).strftime('%Y-%m-%d %H:%M:%S')

    @property
    def html(self):
        return "" \
               "<li>\
                       <div class =\"comment_img\">\
                           <a href = \"profile/%s\"> <img src=\"photo/%s\" class =\"profile_img\" alt=\"Profile\"> </a>\
                           <a href=\"profile/%s\"> %s </a>\
                       </div>\
                       <div class=\"comment_txt\">\
                           %s\
                           <span class=\"time\"> %s </span>\
                       </div>\
               </li>" % (self.user.id, self.user.id, self.user.id, self.user.username, self.comment, self.time)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=True)
    profile = models.ImageField(upload_to='profile/', blank=True)
    age = models.CharField(max_length=3, blank=True)
    biography = models.CharField(max_length=420, null=True)
    userFollowed = models.ManyToManyField(User, symmetrical=False, related_name='userFollowed')

    def __str__(self):
        return self.user.username + ': ' + self.user.first_name + ' ' + self.user.last_name
