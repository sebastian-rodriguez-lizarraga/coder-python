from unittest.util import _MAX_LENGTH
from django import forms 


class ObraFormulario(forms.Form):
      #especificar los campos del form
      nombre = forms.CharField(max_length=50)
      anio = forms.IntegerField()
      estilo= forms.CharField(max_length= 50)


class ArtistaFormulario(forms.Form):
      nombre = forms.CharField(max_length=60)
      apellido = forms.CharField(max_length=60)
      obras = forms.CharField(max_length=90)
      estilo = forms.CharField(max_length=60)

