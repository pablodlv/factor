from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import registro_usuario

# Creo las vistas.

def inicio(request):
    return render(request, 'inicio.html')

def listadoNotas(request):
 notas = Nota.objects.all() 
 contexto= {"notas":notas}
 return render(request, "/listado-notas.html",contexto)

class notasLista(ListView):
    model = Nota
    template_name='/notas_list.html'

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

# Vista de login

def login_request(request):
    if request.method=='POST':
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info['username']
            clave=info['password']
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request,'inicio.html', {'mensaje':f'{usu} iniciaste sesión correctamente'})
            else:
                return render(request,'login.html', {'formmulario':form, 'mensaje':'Datos de ingreso incorrectos'})
        else:
            return render(request,'login.html', {'formmulario':form, 'mensaje':'Datos de ingreso incorrectos'})
    else:
        form=AuthenticationForm()
        return render(request,'login.html', {'formulario':form})
    
# Vista de registro

def registrarse(request):
    if request.method=='POST':
        form=registro_usuario(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre_usuario=info['username']
            form.save()
            return render(request,'inicio.html', {'mensaje':f' Bienvenido, {nombre_usuario}. Gracias por registrarte'})
        else:
            return render(request,'login.html', {'formmulario':form, 'mensaje':'Datos incorrectos'})
    else:
        form=registro_usuario()
        return render(request,'registrarse.html', {'formulario':form})    
