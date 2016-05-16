from django.db import models
from django.contrib.auth.models import User

class Level(models.Model):
    name = models.CharField(max_length=64)
    question = models.TextField()
    multianswer = models.BooleanField(default=False)
    answer = models.CharField(max_length=128)
    sourcehint = models.CharField(max_length=256, blank=True)
    imageurl = models.CharField(max_length=256, blank=True)
    buttontext = models.CharField(max_length=256, blank=True)
    css = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Score(models.Model):
    user = models.OneToOneField(User, editable=False)
    max_level = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)

class Attempt(models.Model):
    user = models.ForeignKey(User)
    level = models.ForeignKey(Level)
    answer = models.TextField()
    correct = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now=True)
