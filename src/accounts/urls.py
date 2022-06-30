from django.urls import path
from accounts.views import login, logout, register

app_name = 'accounts'
urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
] # estaba utilizando los {} que al perecer generaban errores tal vez en el orden