from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render

from core.forms import UserForm

def register(request):

	c = {
	'form': UserForm()
	}

	if request.method != "POST":
		return render (request, "core/register.html", c)

	
	data = request.POST.copy()
	c['form'] = form = UserForm(data)

	if not form.is_valid():
		c['error'] = True
		return render (request, "core/register.html", c)


	if form.cleaned_data['password'] != form.cleaned_data['password2']:
		c['password_mismatch'] = True
		return render (request, "core/register.html", c)
		
	if User.objects.filter(username__iexact=form.cleaned_data['username']).count() > 0:
		c['user_exists'] = True
		return render (request, "core/register.html", c)

	try:
		user = User.objects.create_user (form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
	except:
		c['user_exists'] = True
		return render (request, "core/register.html", c)
	
	user.first_name = form.cleaned_data['first_name']
	user.last_name = form.cleaned_data['last_name']
	user.save()
	
	user = authenticate(username=user.username, password=form.cleaned_data['password'])
	login(request, user)

	return HttpResponseRedirect('/')
