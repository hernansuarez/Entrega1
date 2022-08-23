from django import forms

class PeliculaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    fechaAlquiler= forms.DateField()
    idCliente = forms.IntegerField()
    idSucursal = forms.IntegerField()

class ClienteFormulario(forms.Form):
    idCliente = forms.IntegerField()   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    telefono= forms.CharField(max_length=10)

class SucursalFormulario(forms.Form):
    idSucursal = forms.IntegerField()
    direccion = forms.CharField()