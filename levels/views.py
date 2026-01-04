# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from levels.models import Level, Attempt
from levels.forms import AnswerForm


@login_required
def level(request, pk):
    context = {}
    level = get_object_or_404(Level, pk=pk)
    user = request.user

    if level.get_user_status(user) == "completed":
        return redirect("levellist")

    if user.userprofile.score < level.required_points:
        return redirect("levellist")

    if request.method == "POST":
        answer = request.POST["answer"]
        attempt = Attempt(user=user, level=level, answer=answer)
        # FIXME: should clean this up sometime. should be a couple of functions for reuse
        if level.is_external:
            if level.external_check(answer, user):
                level.set_completed(user)
                attempt.correct = True
                messages.success(request, _("Correct answer. Congrats!"))
                attempt.save()
                return redirect("levellist")
            else:
                attempt.correct = False
                attempt.save()
                messages.error(request, _("Wrong answer! Try again :-D"))

        elif level.check_answer(answer, user):
            level.set_completed(user)
            attempt.correct = True
            messages.success(request, _("Correct answer. Congrats!"))
            attempt.save()
            return redirect("levellist")
        else:
            attempt.correct = False
            attempt.save()
            messages.error(request, _("Wrong answer! Try again :-D"))

    context["level"] = level
    context["form"] = AnswerForm()
    context["attempts"] = user.userprofile.get_attempts(level)
    return render(request, "levels/levels.html", context)


class LevelList(LoginRequiredMixin, ListView):
    model = Level
