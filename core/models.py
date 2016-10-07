from django.db import models
from solo.models import SingletonModel
from django.utils.translation import ugettext as _
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from levels.models import Score

class Config(SingletonModel):
    welcometext = models.TextField(blank=True)
    eventname = models.CharField(max_length=256)
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return _("Site configuration")

    class Meta:
         verbose_name = _("Site configuration")


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    latest_correct_answer = models.DateTimeField(blank=True, null=True)

#    @property
#    def get_score(self):
#        return Score.objects.filter(user=self.user).aggregate(Sum('points'))['points__sum']

#    @property
#    def latest_correct_answer(self):
#        latest = Score.objects.filter(user=self.user).latest('awarded')
#        return latest.awarded


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, signal, created, **kwargs):
    if created:
        UserProfile(user=instance).save()
