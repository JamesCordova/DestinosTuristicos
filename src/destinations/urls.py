from django.urls import path

from .views import (
    destinationsList,
    destinationsShow,
)

urlpatterns = [
    path('', destinationsList, name="lista"),
    path('<int:myID>/', destinationsShow, name="descripcion"),
]