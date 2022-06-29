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
    nombre = forms.CharField(
        widget = forms.Input(
            attrs = {
                'placeholder': 'Ingrese el nombre',
                'label': 'Nombre del lugar',
            }
        )
    )
    img = forms.ImageField()
    descripcion = forms.TextField()
    precio = forms.IntegerField()
    oferta = forms.BooleanField()