from django.shortcuts import render
from django.contrib.auth.models import User,auth
from .forms import RawUserLoginForm


# Create your views here.

def login(request):
    form = RawUserLoginForm(request.POST or None)
    if form.is_valid():
        user = auth.authenticate(**form.cleaned_data)
    else:
        print(form.errors)
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)