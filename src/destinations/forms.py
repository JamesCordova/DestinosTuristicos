from django import forms
from .models import Destination

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = [
            'nombre',
            'img',
            'descripcion',
            'precio',
            'oferta',
        ] # {} era un conjunto, por lo que no habia posiciones, entonces con [] que son listas, los elementos si tienen posicion

class RawDestinationForm(forms.Form):
    nombre = forms.CharField(label = 'Nombre del lugar',
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Ingrese el nombre',
                'class': 'search_input',
            }
        )
    )
    img = forms.ImageField(label = 'Imagen del lugar')
    descripcion = forms.CharField(label = 'Descripcion del lugar',
    widget = forms.Textarea(
        attrs = {
            'placeholder': 'Ingrese la descripcion del lugar',
            'class': 'search_input',
            'cols': 30,
            'rows': 10,
        }
    ))
    precio = forms.IntegerField(
        widget = forms.NumberInput(
            attrs = {
                'placeholder': 'Precio en $',
                'class': 'search_input',
            }
        )
    )
    oferta = forms.BooleanField(required = False)