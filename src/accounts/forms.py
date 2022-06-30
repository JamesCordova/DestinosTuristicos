from django import forms

class RawUserLoginForm(forms.Form):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label='Contraseña',
    widget = forms.PasswordInput(
        attrs = {
            'placeholder': 'Ingrese su contraseña',
        }
    ))
