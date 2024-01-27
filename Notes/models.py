from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField( null = True, blank = True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    created = models.DateTimeField( auto_now_add = True )
    updated = models.DateTimeField( auto_now = True )

    def __str__(self):
        return self.title

