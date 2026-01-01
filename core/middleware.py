from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

from core.models import Config
from levels.models import Level


import re


class ClosedMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if hasattr(request, "user") and request.user.is_staff:
            return None

        if re.match("^/admin/", request.path_info):
            return None
        if re.match("^/__debug__/", request.path_info) and settings.DEBUG:
            return None

        if Config.objects.all().count() != 1:
            return self.closed(request)

        config = Config.objects.get(pk=1)
        if not config.active:
            return self.closed(request)

        if Level.objects.all().count() == 0:
            return self.closed(request)

        return None

    def closed(self, request):
        try:
            config = Config.objects.get(pk=1)
        except Config.DoesNotExist:
            config = {"welcometext": _("This site is not configured yet.")}

        c = {}
        c["config"] = config
        return render(request, "core/closed.html", c)
