# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

from levels.models import Score, Attempt

# score can be accessed by anyone
def score(request):
    context = {}
    context['score'] = Score.objects.order_by('-max_level', 'updated')
    return render(request, "stats/score.html", context)

# attemps should only be visible to superusers
@user_passes_test(lambda u: u.is_superuser)
def attempts(request, getnum=None):
    if getnum == None:
        getnum = 25
    context = {}
    context['getnum'] = getnum
    context['attempts'] = Attempt.objects.order_by('-pk')[:getnum]
    return render(request, "stats/attempts.html", context)
