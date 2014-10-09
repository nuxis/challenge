# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from core.common import prtr

from levels.models import Level, Score, Attempt

from django.http import HttpResponseRedirect, Http404

# score can be accessed by anyone
def score (request):
	c = {}
	c['score'] = Score.objects.order_by ('updated', '-max_level')

	return prtr ("score.html", c, request)


# attemps should only be visible to superusers
@user_passes_test(lambda u: u.is_superuser)
def attempts (request, getnum=None):
	if getnum == None:
		getnum = 25
	
	c = {}
	c['getnum'] = getnum
	c['attempts'] = Attempt.objects.order_by('-pk')[:getnum]

	return prtr ("attempts.html", c, request)
