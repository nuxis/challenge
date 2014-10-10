# Create your views here.


def register(request):
	from challenge.core.common import prtr
	from challenge.core.forms import UserForm
	from django.contrib.auth.models import User
	from django.contrib.auth import login, authenticate
	from django.http import HttpResponseRedirect

	c = {
	'form': UserForm()
	}

	if request.method != "POST":
		return prtr ("core/register.html", c, request)

	
	data = request.POST.copy()
	c['form'] = form = UserForm(data)

	if not form.is_valid():
		c['error'] = True
		return prtr ("core/register.html", c, request)


	if form.cleaned_data['password'] != form.cleaned_data['password2']:
		c['password_mismatch'] = True
		return prtr ("core/register.html", c, request)
		
	if User.objects.filter(username__iexact=form.cleaned_data['username']).count() > 0:
		c['user_exists'] = True
		return prtr ("core/register.html", c, request)

	try:
		user = User.objects.create_user (form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
	except:
		c['user_exists'] = True
		return prtr ("core/register.html", c, request)
	
	user.first_name = form.cleaned_data['first_name']
	user.last_name = form.cleaned_data['last_name']
	user.save()
	
	user = authenticate(username=user.username, password=form.cleaned_data['password'])
	login(request, user)

	return HttpResponseRedirect('/')
