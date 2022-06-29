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