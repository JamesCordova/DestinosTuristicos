from django import forms
from django.contrib.auth.models import User

class RawUserLoginForm(forms.Form):
    username = forms.CharField(label='Usuario',
    widget = forms.PasswordInput(
        attrs = {
            'placeholder': 'Ingrese el usuario',
            'class': 'search_input',
        }
    ))
    password = forms.CharField(label='Contraseña',
    widget = forms.PasswordInput(
        attrs = {
            'placeholder': 'Ingrese su contraseña',
            'class': 'search_input',
        }
    ))

class RawUserRegisterForm(forms.Form):
    first_name = forms.CharField(label='Nombre',
    widget = forms.TextInput(
        attrs = {
            'placeholder': 'Nombres',
            'class': 'search_input',
        }
    ))
    last_name = forms.CharField(label='Apellido',
    widget = forms.TextInput(
        attrs = {
            'placeholder': 'Apellidos',
            'class': 'search_input',
        }
    ))
    username = forms.CharField(label='Usuario',
    widget = forms.TextInput(
        attrs = {
            'placeholder': 'Nombre de usuario',
            'class': 'search_input',
        }
    ))
    email = forms.CharField(label='Correo Electrónico',
    widget = forms.EmailInput(
        attrs = {
            'placeholder': 'Correo electrónico',
            'class': 'search_input',
        }
    ))
    password1 = forms.CharField(label='Contraseña',
    widget = forms.PasswordInput(
        attrs = {
            'placeholder': 'Ingrese su contraseña',
            'class': 'search_input',
        }
    ))
    password2 = forms.CharField(label='Confirmar Contraseña',
    widget = forms.PasswordInput(
        attrs = {
            'placeholder': 'Confirme su contraseña',
            'class': 'search_input',
        }
    ))

    def clean_username(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username = username).exists():
            raise forms.ValidationError('Nombre de usuario existente')
        return username
    
    def clean_password1(self, *args, **kwargs):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password1

    def clean_password2(self, *args, **kwargs):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password1
    
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('Este correo ya es utilizado por otra cuenta')
        return email
    
