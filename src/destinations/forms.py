from django import forms
from .models import Destination

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = {
            'nombre',
            'img',
            'descripcion',
            'precio',
            'oferta',
        }

class RawDestinationForm(forms.Form):
    nombre = forms.CharField(label = 'Nombre del lugar',
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Ingrese el nombre',
            }
        )
    )
    img = forms.ImageField()
    descripcion = forms.CharField()
    precio = forms.IntegerField()
    oferta = forms.BooleanField()