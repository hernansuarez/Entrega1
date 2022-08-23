from django import forms

class PeliculaFormulario(forms.Form):

    #Especificar los campos
    pelicula = forms.CharField()
    genero = forms.CharField()


class ClienteFormulario(forms.Form):
    idCliente = forms.IntegerField()   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    telefono= forms.CharField(max_length=10)

class SucursalFormulario(forms.Form):

    #Especificar los campos
    idSucursal = forms.CharField()
    genero = forms.CharField()