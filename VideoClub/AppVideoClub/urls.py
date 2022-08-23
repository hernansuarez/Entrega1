from django.urls import path
from AppVideoClub import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('Peliculas', views.peliculas, name="Peliculas"),
    path('Clientes', views.clientes, name="Clientes"),
    path('Sucursales', views.sucursales, name="Sucursales"),
    path('buscarCliente/', views.buscarCliente),
    path('buscarPelicula/', views.buscarPelicula),
    path('buscarSucursal/', views.buscarSucursal),

]