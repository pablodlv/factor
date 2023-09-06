from django.urls import path
from Notas.views import listadoNotas

urlpatterns = [
    path('listado-notas/', listadoNotas, name = "ListadoNotas"),
]