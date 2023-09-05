from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Creo las vistas.

def inicio(request):
    return render(request, 'inicio.html')
