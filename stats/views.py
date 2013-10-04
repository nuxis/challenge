# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from challenge.core.common import prtr

from challenge.levels.models import Level, Score

from django.http import HttpResponseRedirect, Http404

#@user_passes_test(lambda u: u.is_superuser)
def score (request):
	c = {}
	c['score'] = Score.objects.order_by ('-max_level')

	return prtr ("score.html", c, request)
