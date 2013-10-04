from django.forms import Form
from django import forms

class UserForm(Form):
	first_name = forms.CharField (max_length=32, label="Fornavn")
	last_name = forms.CharField (max_length=64, label="Etternavn")
	username = forms.CharField (max_length=32, label="Nick")
	email = forms.CharField (max_length=128, label="Email")
	password = forms.CharField (widget=forms.PasswordInput, label="Passord")
	password2 = forms.CharField (widget=forms.PasswordInput, label="Gjenta passord")
