from django import forms
from .models import Problem, User

class ProblemForm(forms.ModelForm):
	class Meta:
		model = Problem
		fields="__all__"



class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields="__all__"
