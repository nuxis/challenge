# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import Config
from levels.models import Level, Score, Attempt
from levels.forms import AnswerForm

@login_required
def index(request):
    context = {}

    try:
        config = Config.objects.get(pk=1)
    except Config.DoesNotExist:
        raise Http404

    context['config'] = config

    if not config.active:
        return render(request, "levels/closed.html", context)

    try:
        end_level = Level.objects.latest('pk')
    except Level.DoesNotExist:
        return render(request, "levels/closed.html", context)

    user = request.user

    try:
        score = Score.objects.get(user=user)
    except:
        score = Score(user=user, max_level=0)


    if score.max_level == end_level.pk:
        return HttpResponseRedirect('/done/')

    level = score.max_level + 1
    level = Level.objects.get(pk=level)

    if request.method == "POST":
        answer = request.POST['answer'].upper()
        attempt = Attempt(user=user, level=level, answer=answer)
        if not level.multianswer:
            if answer == level.answer.upper():
                score.max_level += 1
                score.save()
                attempt.correct = True
                attempt.save()
                return HttpResponseRedirect('/')
            else:
                attempt.correct = False
                attempt.save()
                messages.error(request, _('Wrong answer! Try again :-D'))
        else:
            for level_answer in level.answer.split('||'):
                if answer == level_answer.upper():
                    score.max_level += 1
                    score.save()
                    attempt.correct = True
                    attempt.save()
                    return HttpResponseRedirect('/')
            messages.error(request, _('Wrong answer! Try again :-D'))
            attempt.correct = False
            attempt.save()

    context['level'] = level
    context['form'] = AnswerForm()
    return render(request, "levels/levels.html", context)

@login_required
def done(request):
    context = {}

    try:
        score = Score.objects.get(user=request.user)
    except:
        return HttpResponseRedirect('/')

    end_level = Level.objects.latest('pk')
    if score.max_level == end_level.pk:
        score = Score.objects.get(user=request.user)
        context['score'] = score
        return render(request, "levels/done.html", context)
    else:
        return HttpResponseRedirect('/')


class LevelList(LoginRequiredMixin, ListView):
    model = Level
