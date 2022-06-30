from django.shortcuts import render
from destinations.models import Destination

# Create your views here.

def index(request):
    destinations = Destination.objects.all()
    context = {
        'destinations': destinations,
    }
    return render(request, 'index.html', context)