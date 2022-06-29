from django import forms
from django.contrib.auth.models import User,auth

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        field = [
            'username',
            'password',
        ]
