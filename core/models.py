from django.db import models
from solo.models import SingletonModel
from django.utils.translation import ugettext as _

class Config(SingletonModel):
    welcometext = models.TextField(blank=True)
    eventname = models.CharField(max_length=256)
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return _("Site configuration")

    class Meta:
         verbose_name = _("Site configuration")
