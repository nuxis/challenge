from django.forms import Form
from django import forms
from django.utils.translation import ugettext_lazy as _



class AnswerForm (Form):
	answer = forms.CharField (max_length=128, label=_("Answer"))
