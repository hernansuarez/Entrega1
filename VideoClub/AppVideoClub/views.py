from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppVideoClub.models import Sucursal, Cliente, Pelicula
from AppVideoClub.forms import ClienteFormulario, PeliculaFormulario

# Create your views here.

def inicio(request):

      return render(request, "AppVideoClub/inicio.html")

def sucursal(request):

      return render(request, "AppVideoClub/sucursal.html")


def pelicula(request):

      if request.method == 'POST':

            miFormulario = PeliculaFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  pelicula = Pelicula(nombre=informacion['nombre'], genero=informacion['genero']) 

                  pelicula.save()

                  return render(request, "AppVideoClub/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= PeliculaFormulario() #Formulario vacio para construir el html

      return render(request, "AppVideoClub/pelicula.html", {"miFormulario":miFormulario})




def clientes(request):

      if request.method == 'POST':

            miFormulario = ClienteFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  cliente = Cliente (nombre=informacion['nombre'], apellido=informacion['apellido'], idCliente=informacion['idCliente'],
                  email=informacion['email'],telefono=informacion['telefono'])

                  cliente.save()

                  return render(request, "AppVideoClub/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ClienteFormulario() #Formulario vacio para construir el html

      return render(request, "AppVideoClub/cliente.html", {"miFormulario":miFormulario})




def buscar(request):

      if request.GET["nombre"]:

            nombre = request.GET['nombre']

            cliente = Cliente.objects.filter(nombre__icontains=nombre)

            return render(request, "AppVideoClub/inicio.html", {"clientes":cliente})

      else: 

            respuesta = "No enviaste datos"

      return HttpResponse(respuesta)