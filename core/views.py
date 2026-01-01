from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from django.db import IntegrityError

from core.forms import UserForm


@login_required
def index(request):
    return redirect("levellist")


def register(request):
    context = {"form": UserForm()}

    if request.method != "POST":
        return render(request, "core/register.html", context)

    data = request.POST.copy()
    context["form"] = form = UserForm(data)

    error = False

    if not form.is_valid():
        messages.error(request, _("Something went wrong, check the form and try again"))
        error = True

    if form.cleaned_data["password"] != form.cleaned_data["password2"]:
        messages.error(request, _("The passwords you entered did not match"))
        error = True

    if User.objects.filter(username__iexact=form.cleaned_data["username"]).count() > 0:
        messages.error(request, _("Username already exists"))
        error = True

    if error:
        return render(request, "core/register.html", context)

    try:
        user = User.objects.create_user(
            form.cleaned_data["username"],
            form.cleaned_data["email"],
            form.cleaned_data["password"],
        )
    except IntegrityError:
        messages.error(request, _("Username already exists"))
        return render(request, "core/register.html", context)
    except ValueError:
        messages.error(request, _("Invalid input"))
        return render(request, "core/register.html", context)

    user.first_name = form.cleaned_data["first_name"]
    user.last_name = form.cleaned_data["last_name"]
    user.save()

    user = authenticate(username=user.username, password=form.cleaned_data["password"])
    login(request, user)

    return HttpResponseRedirect("/")
