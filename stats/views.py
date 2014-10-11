# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404

from levels.models import Level, Score, Attempt


# score can be accessed by anyone
def score (request):
	c = {}
	c['score'] = Score.objects.order_by ('-max_level', 'updated')

	return render (request, "score.html", c)


# attemps should only be visible to superusers
@user_passes_test(lambda u: u.is_superuser)
def attempts (request, getnum=None):
	if getnum == None:
		getnum = 25
	
	c = {}
	c['getnum'] = getnum
	c['attempts'] = Attempt.objects.order_by('-pk')[:getnum]

	return render (request, "attempts.html", c)
