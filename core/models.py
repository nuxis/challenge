from django.db import models
from solo.models import SingletonModel
from django.utils.translation import gettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User


class Config(SingletonModel):
    welcometext = models.TextField(blank=True)
    eventname = models.CharField(max_length=256)
    active = models.BooleanField(default=False)
    webhook_admins = models.CharField(
        max_length=512,
        help_text="Slack-compatible webhooks for admins. May contain game-sensitive information",
        default=None,
        null=True,
        blank=True,
    )

    def __str__(self):
        return _("Site configuration")

    class Meta:
        verbose_name = _("Site configuration")


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    latest_correct_answer = models.DateTimeField(blank=True, null=True)

    def get_attempts(self, level):
        return len(self.user.attempt_set.filter(level=level))

    @property
    def rank(self):
        users_sorted = UserProfile.objects.all().order_by(
            "-score", "latest_correct_answer"
        )
        for index, item in enumerate(users_sorted):
            if item.pk == self.pk:
                return index + 1


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, signal, created, **kwargs):
    if created:
        UserProfile(user=instance).save()
