from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=42)

    def __str__(self):
        return self.user.username + ' ' + self.comment + ' ' + self.time


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=True)
    profile = models.ImageField(upload_to='profile/', blank=True)
    age = models.CharField(max_length=3, blank=True)
    biography = models.CharField(max_length=420, null=True)
    userFollowed = models.ManyToManyField(User, symmetrical=False, related_name='userFollowed')

    def __str__(self):
        return self.user.username + ': ' + self.user.first_name + ' ' + self.user.last_name
