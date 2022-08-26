from django.shortcuts import render
from .models import Familiar # importo la clase que cree en modelo 
from django.template import Context, Template
from django.http import HttpResponse 

def familiar(request):
    familiar0 = Familiar(nombre="Nahuel",apellido="Huapi",edad= 806,cumple="1921-9-12")
    familiar1 = Familiar(nombre="Dario",apellido="Pipa",edad= 34,cumple="1921-9-12")
    familiar2 = Familiar(nombre="Julian",apellido="Alvarez",edad= 30,cumple="1921-9-12")
    familiar0.save()
    familiar1.save()
    familiar2.save()

    #ordenados respectivamente el primero con el primero el segundo con el segundo...
    personas = {"nombre0":familiar0.nombre,"apellido0":familiar0.apellido,"edad0":familiar0.edad, "cumple0":familiar0.cumple,"nombre1":familiar1.nombre,"apellido1":familiar1.apellido,"edad1":familiar1.edad,"cumple1":familiar1.cumple,"nombre2":familiar2.nombre,"apellido2":familiar2.apellido,"edad2":familiar2.edad,"cumple2":familiar2.cumple}
    mihtml=open("C:/Users/rodri/OneDrive/Documents/CursoDePyhton/pildora_proy/Proyecto1/Proyecto1/templates/mifamilia.html")
    plantilla=Template(mihtml.read())
    mihtml.close()
    contexto= Context(personas)
    documento=plantilla.render(contexto)
    return HttpResponse(documento)