from this import d
from django.db import models

# Create your models here.
# 
class Familiar(models.Model):
    nombre = models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    edad = models.IntegerField()
    cumple= models.DateField()

    def __str__(self) :
        return self.nombre+" "+str(self.apellido)


class Artista(models.Model):
    nombre= models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    obras = models.CharField(max_length=120)
    estilo = models.CharField(max_length=80)
    def __str__(self) :
        return self.nombre+" "+str(self.apellido)

class ObraDeArte(models.Model):
     nombre= models.CharField(max_length=60)
     anio = models.IntegerField()
     estilo = models.CharField(max_length=80)

     def __str__(self) :
        return self.nombre+" "+str(self.anio)