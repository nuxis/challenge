from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from core.models import Config
from core.tasks import web_post_json

class Level(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)

    points = models.IntegerField(default=1)
    completed = models.IntegerField(default=0)

    question = models.TextField()
    multianswer = models.BooleanField(default=False)
    answer = models.CharField(max_length=128)
    sourcehint = models.CharField(max_length=256, blank=True)
    imageurl = models.CharField(max_length=256, blank=True)
    buttontext = models.CharField(max_length=256, blank=True)
    css = models.TextField(blank=True)

    required_points = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def set_completed(self, user):
        self.completed += 1
        self.save()

        score = Score(user=user, level=self, points=self.points)
        score.save()

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
    user = models.ForeignKey(User)
    level = models.ForeignKey(Level)
    points = models.IntegerField()
    awarded = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=Score)
def updated_score(sender, instance, signal, created, **kwargs):
    if created:
        # update score in user profile
        user = instance.user
        userprofile = user.userprofile
        userprofile.latest_correct_answer = timezone.now()
        userprofile.score += instance.points
        userprofile.save()

        # send webhook if configured
        # FIXME: translation of webhook payload?
        config = Config.objects.get(pk=1)
        if config.webhook_admins:
            web_post_json.delay(
                config.webhook_admins,
                {'text': '{} completed level {} for {} points'.format(instance.user, instance.level, instance.points)}
            )


class Attempt(models.Model):
    user = models.ForeignKey(User)
    level = models.ForeignKey(Level)
    answer = models.TextField()
    correct = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now=True)
