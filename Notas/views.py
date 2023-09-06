from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Nota

# Creo las vistas.

def inicio(request):
    return render(request, 'inicio.html')

class NotasList(ListView):
    model = Nota
    template_name='archivo.html'
