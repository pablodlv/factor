from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .models import *

# Creo las vistas.

def inicio(request):
    return render(request, 'inicio.html')

def listadoNotas(request):
 notas = Nota.objects.all() 
 contexto= {"notas":notas}
 return render(request, "Notas/listado-notas.html",contexto)

class notasLista(ListView):
    model = Nota
    template_name='Notas/notas_list.html'

# Vista de búsquedas y resultados

def busquedaNotas(request):
    return render(request,'busqueda_nota.html')

def busquedaNota(request):
    titulo=request.GET['titulo']
    if titulo!='':
        notas=Nota.objects.filter(titulo__icontains=titulo)
        return render(request,'resultados_notas.html', {'nota':notas})
    else:
        return render(request,'busqueda_notas.html', {'mensaje':'Por favor, ingresá algún término de búsqueda'})
