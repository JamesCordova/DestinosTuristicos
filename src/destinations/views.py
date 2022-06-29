from django.shortcuts import render
from .models import Destination

# Create your views here.

def destinationsList(request):
    queryset = Destination.objects.all()
    context = {
        'objectList': queryset,
    }
    return render(request, 'destinations/destinations.html', context)