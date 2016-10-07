# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.views.generic import ListView
from core.models import UserProfile

from levels.models import Score, Attempt

# score can be accessed by anyone
class ScoreList(ListView):
#    queryset = User.objects.filter(is_superuser=False).filter(is_staff=False)
    model = UserProfile
    template_name = 'stats/score_list.html'

    ordering = ['-score', '-latest_correct_answer']


# attemps should only be visible to superusers
@user_passes_test(lambda u: u.is_superuser)
def attempts(request, getnum=None):
    if getnum == None:
        getnum = 25
    context = {}
    context['getnum'] = getnum
    context['attempts'] = Attempt.objects.order_by('-pk')[:getnum]
    return render(request, "stats/attempts.html", context)
