from django.shortcuts import render
from destinations.models import Destination
from django.views.generic import (
    ListView,
)

# Create your views here.
class Index(ListView):
    model = Destination
    template_name = "index.html"
    