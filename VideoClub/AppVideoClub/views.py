from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppVideoClub.models import Sucursal, Cliente, Pelicula
from AppVideoClub.forms import ClienteFormulario, PeliculaFormulario, SucursalFormulario

# Create your views here.

def inicio(request):

      return render(request, "AppVideoClub/inicio.html")

def sucursal(request):

      return render(request, "AppVideoClub/sucursal.html")


def pelicula(request):

      return render(request, "AppVideoClub/pelicula.html")


def clientes(request):

      if request.method == 'POST':

            miFormulario = ClienteFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  cliente = Cliente (nombre=informacion['nombre'], apellido=informacion['apellido'], idCliente=informacion['idCliente'],
                  email=informacion['email'],telefono=informacion['telefono'])

                  cliente.save()

                  return render(request, "AppVideoClub/inicio.html")

      else: 

            miFormulario= ClienteFormulario()

      return render(request, "AppVideoClub/cliente.html", {"miFormulario":miFormulario})



def buscar(request):

      if request.GET["nombre"]:

            nombre = request.GET['nombre']

            cliente = Cliente.objects.filter(nombre__icontains=nombre)

            return render(request, "AppVideoClub/inicio.html", {"clientes":cliente})

      else: 

            respuesta = "No enviaste datos"

      return HttpResponse(respuesta)