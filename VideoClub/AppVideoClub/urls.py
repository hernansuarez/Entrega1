from django.urls import path
from AppVideoClub import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('Peliculas', views.pelicula, name="Peliculas"),
    path('Clientes', views.clientes, name="Clientes"),
    path('Sucursales', views.sucursal, name="Sucursales"),
    path('buscar/', views.buscar),

]