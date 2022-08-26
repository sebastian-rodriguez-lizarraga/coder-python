from datetime import datetime
from django.http import HttpResponse 
import datetime
from django.shortcuts import render 
from django.template import Template, Context

def saludo(request):  #primera vista
    doc_externo = open("C:/Users/rodri/OneDrive/Documents/CursoDePyhton\pildora_proy/Proyecto1/Proyecto1/templates/miplantilla.html")
    plt = Template(doc_externo.read())
    doc_externo.close()

    #crear el contexto
    ctx = Context()
    #almaceno el renderizado del documento con el contexto

    documento = plt.render(ctx)


    return HttpResponse(documento)

def despedida(request):

    return HttpResponse("Hasta luego alumnos de django")


def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    
    documento ="la fecha hoy es %s"  %fecha_actual
    return HttpResponse(documento)

def calculaEdad(request,edad, anio):
    edadActual=18
    periodo=anio-2019
    edadFutura = edad + periodo
    documento="<html> <body> <h2> En el año %s tendrás %s años  </h2> </body> </html>"  %(anio,edadFutura)

    return HttpResponse(documento)



