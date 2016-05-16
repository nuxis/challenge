from django.db import models
from django.contrib.auth.models import User

class Level(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)

    question = models.TextField()
    multianswer = models.BooleanField(default=False)
    answer = models.CharField(max_length=128)
    sourcehint = models.CharField(max_length=256, blank=True)
    imageurl = models.CharField(max_length=256, blank=True)
    buttontext = models.CharField(max_length=256, blank=True)
    css = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_user_status(self, user):
        # XXX: this could need optimizing later. is called from a templatetag, and runs a query per level or more...
        
        attempts = self.attempt_set
        if attempts.filter(correct=True):
            return "completed"
        if attempts.count() > 0:
            return "tried"
        else:
            return False

    class Meta():
        managed = True


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
