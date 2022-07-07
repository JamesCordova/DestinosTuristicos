from django.urls import path

from .views import (
    destinationsList,
    destinationsShow,
    destinationsCreate,
    destinationsEdit,
    destinationsDelete,
)

app_name = 'destinations'
urlpatterns = [
    path('', destinationsList, name="lista"),
    path('<int:myID>/', destinationsShow, name="descripcion"),
    path('create/', destinationsCreate, name="crear"),
    path('<int:myID>/edit/', destinationsEdit, name="editar"),
    path('<int:myID>/delete/', destinationsDelete, name="eliminar"),
    path('403/', destinationsDelete, name="sin-acceso"),
]