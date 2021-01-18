from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

User = get_user_model()


class LoginForm( forms.Form ):
	username = forms.CharField()
	password = forms.CharField(
		widget=forms.PasswordInput
	)

class CreateUserForm(UserCreationForm):
	password1 = forms.CharField(
		label="Password",
		widget=forms.PasswordInput(
			attrs={'class':'w-full p-2 mt-1 bg-gray-200 rounded-md focus:outline-none', 'type':'password'}),
	)
	password2 = forms.CharField(
		label="Confirm password",
		widget=forms.PasswordInput(
			attrs={'class':'w-full p-2 mt-1 bg-gray-200 rounded-md focus:outline-none', 'type':'password'}),
	)
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		widgets = {
			'username': forms.TextInput(
				attrs={'class': 'w-full p-2 mt-1 bg-gray-200 rounded-md focus:outline-none'}),
			'email': forms.EmailInput(
				attrs={'class': 'w-full p-2 mt-1 bg-gray-200 rounded-md focus:outline-none'}),
		}