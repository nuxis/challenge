# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from challenge.core.common import prtr

from challenge.levels.models import Level, Score, Attempt

from django.http import HttpResponseRedirect, Http404

# vise score til alle, f.eks. på projektor
#@user_passes_test(lambda u: u.is_superuser)
def score (request):
	c = {}
	c['score'] = Score.objects.order_by ('-max_level')

	return prtr ("score.html", c, request)

# svarene kun til admins
@user_passes_test(lambda u: u.is_superuser)
def attempts (request):
	c = {}
	c['attempts'] = Attempt.objects.order_by('-pk')

	return prtr ("attempts.html", c, request)
