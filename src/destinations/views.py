from django.shortcuts import render, redirect
from .models import Destination
from .forms import DestinationForm, RawDestinationForm

# Create your views here.

def destinationsList(request):
    queryset = Destination.objects.all()
    context = {
        'destinations': queryset,
    }
    return render(request, 'destinations/destinations.html', context)

def destinationsShow(request, myID):
    obj = Destination.objects.get(id = myID)
    context = {
        'dest': obj,
    }
    return render(request, 'destinations/destinationsShow.html', context)

def destinationsCreate(request):
    form = RawDestinationForm()
    if request.method == 'POST':
        form = RawDestinationForm(request.POST, request.FILES) # segun: https://www.geeksforgeeks.org/imagefield-django-forms/ es necesario el request.FILES en el views.py y el enctype="mulitpart/form-data" en el html
        if form.is_valid():
            print(form.cleaned_data)
            obj = Destination.objects.create(**form.cleaned_data)
            return redirect('../')
        else:
            print(form.errors)
    context = {
        'form': form,
    }
    return render(request, 'destinations/destinationsCreate.html', context)

def destinationsEdit(request, myID):
    obj = Destination.objects.get(id = myID)
    form = DestinationForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        form = DestinationForm()
    context = {
        'form': form,
    }
    return render(request, 'destinations/personasCreate.html', context)
