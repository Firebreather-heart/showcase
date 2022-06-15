from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = get_user_model()
		fields = ('username', 'email', 'date_of_birth', )
		widget = {
			'username': forms.TextInput(
				attrs={
					'placeholder': 'Username',  'type': 'text',
					'name': 'username',
					}
				),
			'email': forms.EmailInput(
				attrs={
					'placeholder': 'E-mail',  'type': 'email', 'name': 'email',
					}
				),
			'date_of_birth': forms.DateInput(attrs={
				'placeholder': 'Date of Birth',  'type': 'date', 'name': 'dob'
				}),
				
			}


class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = get_user_model()
		fields = ('username', 'email', 'date_of_birth', )
		widget = {
			'username': forms.TextInput(
				attrs={
					'placeholder': 'Username',  'type': 'text',
					'name': 'username',
					}
				),
			'email': forms.EmailInput(
				attrs={
					'placeholder': 'E-mail',  'type': 'email', 'name': 'email',
					}
				),
			'date_of_birth': forms.DateInput(attrs={
				'placeholder': 'Date of Birth',  'type': 'date', 'name': 'dob'
				}),
			}