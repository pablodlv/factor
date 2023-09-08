from django.urls import path
from Notas.views import notasLista

urlpatterns = [
    
    #path('listadoNotas/', listadoNotas, name = "listadoNotas"),
    path('notas/list/', notasLista.as_view(), name='listado_notas'),
]