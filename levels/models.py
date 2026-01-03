from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from core.models import Config
from core.tasks import web_post_json


class Level(models.Model):
    name = models.CharField(max_length=64, help_text="Shown in level list.")
    description = models.CharField(max_length=128, help_text="Shown in level list.")

    points = models.IntegerField(
        default=1, help_text="How many points is this level worth?"
    )
    completed = models.IntegerField(
        default=0, help_text="Number of users that solved this level."
    )

    is_external = models.BooleanField(
        default=False,
        help_text="Check answer against URL in answer field",
    )

    question = models.TextField(
        blank=True,
        help_text="Question-text. Can be empty, but then you should have some other way (image?) for users to understand the question.",
    )
    multianswer = models.BooleanField(
        default=False,
        help_text='Multiple possible answers? Split answers with "||" in the answer field.',
    )
    answer = models.CharField(
        max_length=256,
        help_text='Answer here. If multianswer, split with "||". If external, URL here.',
    )
    sourcehint = models.CharField(max_length=256, blank=True)
    imageurl = models.CharField(
        max_length=256,
        blank=True,
        help_text="URL to image to be shown on the level page. Uploads must be handled outside of challenge.",
    )
    buttontext = models.CharField(
        max_length=256,
        blank=True,
        help_text='Text for the submit button. Default is "Feeling lucky? ;-)"',
    )
    css = models.TextField(
        blank=True, help_text="This field will be inserted into the level page as CSS"
    )
    javascript = models.TextField(
        blank=True,
        help_text="This field will be inserted into the level page as JavaScript",
    )

    required_points = models.IntegerField(
        default=0, help_text="Number of points required to access this level."
    )
    required_attempts = models.PositiveIntegerField(
        default=0,
        help_text="Users need to try at least this many times before we accept an answer",
    )

    def __str__(self):
        return self.name

    def set_completed(self, user):
        self.completed += 1
        self.save()

        score = Score(user=user, level=self, points=self.points)
        score.save()

    def check_answer(self, answer, user):
        if (
            self.required_attempts
            and self.required_attempts > user.userprofile.get_attempts(self)
        ):
            return False

        answer = answer.upper()
        level_answer = self.answer.upper()

        if self.multianswer and answer in level_answer.split("||"):
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

    def external_check(self, attempted_answer, user):
        timeout = 10  # XXX: hardcoded timeout for external answer check
        url = self.answer  # URL is stored in level answer field
        payload = {
            "level_name": self.name,
            "level_pk": self.pk,
            "attempted_answer": attempted_answer,
            "user_username": user.username,
            "user_pk": user.pk,
        }
        response = web_post_json(url, payload, timeout)
        if response == 200:
            return True
        else:
            return False


class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    points = models.IntegerField()
    awarded = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=Level)
def updated_level(sender, instance, signal, created, **kwargs):
    if created:
        # send webhook if configured
        # FIXME: translation of webhook payload?
        config = Config.objects.get()
        if config.webhook_admins:
            web_post_json.delay(
                config.webhook_admins,
                {
                    "attachments": [
                        {
                            "fallback": "New level created: {}".format(instance.name),
                            "text": "New level created: *{}*".format(instance.name),
                            "mrkdwn_in": ["text", "pretext"],
                        }
                    ]
                },
            )


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
        config = Config.objects.get()
        if config.webhook_admins:
            web_post_json.delay(
                config.webhook_admins,
                {
                    "attachments": [
                        {
                            "fallback": "{} completed level {} for {} points".format(
                                instance.user, instance.level, instance.points
                            ),
                            "text": "User *{}* completed level *{}* for *{}* points. ".format(
                                instance.user, instance.level, instance.points
                            ),
                            "fields": [
                                {
                                    "title": "Current rank",
                                    "short": True,
                                    "value": "{}".format(
                                        instance.user.userprofile.rank
                                    ),
                                },
                                {
                                    "title": "Total points",
                                    "short": True,
                                    "value": "{}".format(
                                        instance.user.userprofile.score
                                    ),
                                },
                            ],
                            "color": "good",
                            "mrkdwn_in": ["text", "pretext"],
                        }
                    ]
                },
            )


class Attempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    answer = models.TextField()
    correct = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now=True)
