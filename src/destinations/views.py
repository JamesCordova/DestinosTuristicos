from django.shortcuts import get_object_or_404, render, redirect
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
    if not(request.user.is_authenticated):# no halle forma que fuese solo una funcion
        return redirect('/accounts/login')
    if not(request.user.is_staff):
        return redirect('/403/')
    obj = get_object_or_404(Destination, id = myID)
    context = {
        'dest': obj,
    }
    return render(request, 'destinations/destinationsShow.html', context)

def destinationsCreate(request):
    if not(request.user.is_authenticated):
        return redirect('/accounts/login')
    if not(request.user.is_staff):
        return redirect('/403/')
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
    if not(request.user.is_authenticated):
        return redirect('/accounts/login')
    if not(request.user.is_staff):
        return redirect('/403/')
    obj = get_object_or_404(Destination, id = myID)
    form = DestinationForm(request.POST or None, request.FILES or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('../')
    context = {
        'form': form,
    }
    return render(request, 'destinations/destinationsCreate.html', context)

def destinationsDelete(request, myID):
    if not(request.user.is_authenticated):
        return redirect('/accounts/login')
    if not(request.user.is_staff):
        return redirect('/403/')
    obj = get_object_or_404(Destination, id = myID)
    if request.method == 'POST':
        print('Se borro el elemento')
        obj.delete()
        return redirect('../../')
    context = {
        'dest': obj,
    }
    return render(request, 'destinations/destinationsDelete.html', context)

def noAccess(request):
    context = {}
    return render(request, 'destinations/403.html', context)