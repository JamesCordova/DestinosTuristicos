from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import RawUserLoginForm, RawUserRegisterForm


# Create your views here.

def login(request):
    form = RawUserLoginForm(request.POST or None)
    if form.is_valid():
        user = auth.authenticate(**form.cleaned_data)
        if user is not None:
            auth.login(request, user)
            return redirect('../../')
        else:
            messages.info(request, 'Credenciales inválidas')
    else:
        print(form.errors)
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    form = RawUserRegisterForm(request.POST or None)
    if form.is_valid():
        user = User.objects.create_user(
            username = form.cleaned_data.get('username'),
            password = form.cleaned_data.get('password1'),
            email = form.cleaned_data.get('email'),
            first_name = form.cleaned_data.get('first_name'),
            last_name = form.cleaned_data.get('last_name')
        )# no encontre forma de hacerlo mediante el form.cleaned_data
        user.save()
    else:
        print(form.errors)
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)