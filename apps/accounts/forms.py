from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

