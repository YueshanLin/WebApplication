from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    time = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=42)

    def __str__(self):
        return self.user.username + ' ' + self.comment + ' ' + self.time

