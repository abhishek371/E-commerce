from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control col-8", "placeholder": "Username"}
))
	password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control col-8","placeholder": "Password"}))




class RegisterForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control col-8", "placeholder": "Username"}
))
	email    = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control col-8", "placeholder": "Email"}
))
	password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control col-8","placeholder": "Password"}))
	password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={"class": "form-control col-8","placeholder": "Confirm Password"}))

	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password2 != password:
			raise forms.ValidationError("Passwords must match.")
		return data

	def clean_username(self):
		username = self.cleaned_data.get('username')
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("Username is taken")
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("email is taken")
		return email

