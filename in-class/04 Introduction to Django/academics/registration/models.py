from django.db import models


class Item(model.Model):
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text

