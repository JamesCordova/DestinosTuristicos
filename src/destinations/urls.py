from django.urls import path

from .views import (
    destinationsList,
    destinationsShow,
    destinationsCreate,
)

urlpatterns = [
    path('', destinationsList, name="lista"),
    path('<int:myID>/', destinationsShow, name="descripcion"),
    path('create/', destinationsCreate, name="crear"),
]