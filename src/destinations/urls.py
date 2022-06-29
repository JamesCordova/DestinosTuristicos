from django.urls import path

from .views import destinationsList

urlpatterns = [
    path('', destinationsList, name="lista"),
    path('<int:myID>/', destinationsList, name="descripcion"),
]