from django.db import models
from django.contrib.auth.models import User

class Level(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)

    points = models.IntegerField()

    question = models.TextField()
    multianswer = models.BooleanField(default=False)
    answer = models.CharField(max_length=128)
    sourcehint = models.CharField(max_length=256, blank=True)
    imageurl = models.CharField(max_length=256, blank=True)
    buttontext = models.CharField(max_length=256, blank=True)
    css = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def check_answer(self, answer):
        answer = answer.upper()
        level_answer = self.answer.upper()

        if self.multianswer and answer in level_answer.split('||'):
            return True
        elif not self.multianswer and answer == level_answer:
            return True
        else:
            return False


    def get_user_status(self, user):
        # XXX: this could need optimizing later. is called from a templatetag, and runs a query per level or more...
        
        attempts = self.attempt_set.filter(user=user)
        if attempts.filter(correct=True):
            return "completed"
        if attempts.count() > 0:
            return "tried"
        else:
            return False


class Score(models.Model):
    user = models.OneToOneField(User)
    level = models.OneToOneField(Level)
    points = models.IntegerField()
    awarded = models.DateTimeField(auto_now_add=True)


class Attempt(models.Model):
    user = models.ForeignKey(User)
    level = models.ForeignKey(Level)
    answer = models.TextField()
    correct = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now=True)
