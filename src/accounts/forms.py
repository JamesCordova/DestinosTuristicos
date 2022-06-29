from django import forms
from django.contrib.auth.models import User,auth

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        field = [
            'username',
            'password',
        ]

class RawUserLoginForm(forms.Form):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label='Contraseña')
