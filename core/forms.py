from django.forms import Form
from django import forms
from django.utils.translation import gettext_lazy as _


class UserForm(Form):
    first_name = forms.CharField(max_length=32, label=_("Firstname"))
    last_name = forms.CharField(max_length=64, label=_("Lastname"))
    username = forms.CharField(max_length=32, label=_("Username"))
    email = forms.CharField(max_length=128, label=_("Email"))
    password = forms.CharField(widget=forms.PasswordInput, label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput, label=_("Repeat passord"))
