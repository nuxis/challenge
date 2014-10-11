# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required

from core.common import prtr

from core.models import Config
from levels.models import Level, Score, Attempt

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404

@login_required
def index(request):
    c = {}
    
    try:
        config = Config.objects.get(pk=1)
    except Config.DoesNotExist:
        raise Http404

    c['config'] = config
    
    if not config.active:
        return prtr ("closed.html", c, request)
    
    try:
        end_level = Level.objects.latest('pk')
    except Level.DoesNotExist:
        return render (request, "closed.html", c)

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
        attempt = Attempt (user=user, level=level, answer=answer)
        if not level.multianswer:
            if answer == level.answer.upper():
                score.max_level += 1
                score.save()
                attempt.correct = True
                attempt.save ()
                return HttpResponseRedirect('/')
            else:
                attempt.correct = False
                attempt.save ()
                c['error'] = 'Feil svar! Prøv igjen :-D'
        else:
            for level_answer in level.answer.split('||'):
                if answer == level_answer.upper():
                    score.max_level += 1
                    score.save()
                    attempt.correct = True
                    attempt.save ()
                    return HttpResponseRedirect('/')
            c['error'] = 'Feil svar! Prøv igjen :-D'
            attempt.correct = False
            attempt.save ()
            
    c['level'] = level

    return prtr("levels.html", c, request)

@login_required
def done(request):
    c = {}

    try:
        score = Score.objects.get(user=request.user)
    except:
        return HttpResponseRedirect('/')
        

    end_level = Level.objects.latest('pk')
    if score.max_level == end_level.pk:
            score = Score.objects.get(user=request.user)
            c['score'] = score

            return prtr ("done.html", c, request)
    else:
        return HttpResponseRedirect('/')
