from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control col-8", "placeholder": "Username"}
))
	password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control col-8","placeholder": "Password"}))
