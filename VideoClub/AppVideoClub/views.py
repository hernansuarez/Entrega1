from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppVideoClub.models import Sucursal, Cliente, Pelicula
from AppVideoClub.forms import ClienteFormulario, PeliculaFormulario, SucursalFormulario

# Create your views here.

def inicio(request):

      return render(request, "AppVideoClub/inicio.html")


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



def peliculas(request):

      if request.method == 'POST':

            miFormulario = PeliculaFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  pelicula = Pelicula (nombre=informacion['nombre'], genero=informacion['genero'], idCliente=informacion['idCliente'],
                  idSucursal=informacion['idSucursal'], fechaAlquiler=informacion['fechaAlquiler'])

                  pelicula.save()

                  return render(request, "AppVideoClub/inicio.html")

      else: 

            miFormulario= PeliculaFormulario()

      return render(request, "AppVideoClub/pelicula.html", {"miFormulario":miFormulario})

      
def sucursales(request):

      if request.method == 'POST':

            miFormulario = SucursalFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  sucursal = Sucursal (idSucursal=informacion['idSucursal'], direccion=informacion['direccion'])

                  sucursal.save()

                  return render(request, "AppVideoClub/inicio.html")

      else: 

            miFormulario= SucursalFormulario()

      return render(request, "AppVideoClub/sucursal.html", {"miFormulario":miFormulario})




def buscarCliente(request):

      if request.GET["nombre"]:

            nombre = request.GET['nombre']

            cliente = Cliente.objects.filter(nombre__icontains=nombre)

            return render(request, "AppVideoClub/inicio.html", {"cliente":cliente})

      else: 

            respuesta = "No enviaste datos"

      return HttpResponse(respuesta)

def buscarPelicula(request):

      if request.GET["nombre"]:

            nombre = request.GET['nombre']

            pelicula = Pelicula.objects.filter(nombre__icontains=nombre)

            return render(request, "AppVideoClub/inicio.html", {"pelicula":pelicula})

      else: 

            respuesta = "No enviaste datos"

      return HttpResponse(respuesta)


def buscarSucursal(request):

      if request.GET["direccion"]:

            direccion = request.GET['direccion']

            sucursal = Sucursal.objects.filter(direccion__icontains=direccion)

            return render(request, "AppVideoClub/inicio.html", {"sucursal":sucursal})

      else: 

            respuesta = "No enviaste datos"

      return HttpResponse(respuesta)