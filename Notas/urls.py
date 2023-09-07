from django.urls import path
from Notas.views import listadoNotas

urlpatterns = [
    
    path('listadoNotas/', listadoNotas, name = "listadoNotas"),
]