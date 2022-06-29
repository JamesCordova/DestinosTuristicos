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
    img = forms.ImageField(label = 'Imagen del lugar')
    descripcion = forms.CharField(label = 'Descripcion del lugar',
    widget = forms.Textarea(
        attrs = {
            'placeholder': 'Ingrese la descripcion del lugar',
            'cols': 30,
            'rows': 10,
        }
    ))
    precio = forms.IntegerField()
    oferta = forms.BooleanField()