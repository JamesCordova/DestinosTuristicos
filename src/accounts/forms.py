from django import forms

class RawUserLoginForm(forms.Form):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label='Contraseña',
    widget = forms.PasswordInput(
        attrs = {
            'placeholder': 'Ingrese su contraseña',
        }
    ))

class RawUserRegisterForm(forms.Form):
    first_name = forms.CharField(label='Nombre',
    widget = forms.TextInput(
        attrs = {
            'placeholder': 'Nombres',
        }
    ))
    last_name = forms.CharField(label='Apellido',
    widget = forms.TextInput(
        attrs = {
            'placeholder': 'Apellidos',
        }
    ))
    username = forms.CharField(label='Usuario',
    widget = forms.TextInput(
        attrs = {
            'placeholder': 'Nombre de usuario',
        }
    ))
    email = forms.CharField(label='Correo Electrónico',
    widget = forms.EmailInput(
        attrs = {
            'placeholder': 'Correo electrónico',
        }
    ))
    password1 = forms.CharField(label='Contraseña',
    widget = forms.PasswordInput(
        attrs = {
            'placeholder': 'Ingrese su contraseña',
        }
    ))
    password2 = forms.CharField(label='Confirmar Contraseña',
    widget = forms.PasswordInput(
        attrs = {
            'placeholder': 'Ingrese de nuevo su contraseña',
        }
    ))
