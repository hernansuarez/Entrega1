from django.db import models

# Create your models here.
class Pelicula(models.Model):
    nombre= models.CharField(max_length=30)
    genero= models.CharField(max_length=30)
    fechaAlquiler= models.DateField()
    idCliente = models.IntegerField()
    idSucursal = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - genero {self.genero}"

class Cliente(models.Model):

    idCliente = models.IntegerField()
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    telefono= models.CharField(max_length=10)

    def __str__(self):
        return f"Nombre: {self.nombre} - idCliente {self.idCliente}"

class Sucursal(models.Model):
    idSucursal = models.IntegerField()
    direccion = models.CharField(max_length=30)