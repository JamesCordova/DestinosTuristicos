from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import RawUserLoginForm


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