from django.shortcuts import render
from .models import Familiar, ObraDeArte,Artista # importo la clase que cree en modelo 
from django.template import Context, Template
from django.http import HttpResponse 
from familia.forms import ObraFormulario,ArtistaFormulario



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




def inicio(request):
    return render (request, "familia/inicio.html")
     
def obras_de_arte(request):
     return render(request, "familia/obras_de_arte.html")

def artistaas(request):
         return render(request, "familia/artistas.html")


""""

view para formulario a mano

def obraFormulario(request):
    if request.method=="POST":
      #  miFormulario = ObraFormulario(request.POST)
        nombre=request.POST.get("nombre")
        anio=request.POST.get("anio")
        estilo=request.POST.get("estilo")
        obra= ObraDeArte(nombre=nombre,anio=anio,estilo=estilo)
        obra.save()
        return render(request, "familia/inicio.html")
    return render(request, "familia/obraFormulario.html")
"""

def obraFormulario(request):
    if request.method=="POST":
        miFormulario = ObraFormulario(request.POST)
        """"
        nombre=request.POST.get("nombre")
        anio=request.POST.get("anio")
        estilo=request.POST.get("estilo")

        """
        if miFormulario.is_valid():
            info= miFormulario.cleaned_data
            print(info)
            nombre=info.get("nombre")
            anio=info.get("anio")
            estilo=info.get("estilo")
            obra= ObraDeArte(nombre=nombre,anio=anio,estilo=estilo)
            obra.save()
            return render(request, "familia/inicio.html",{"mensaje":"Obra creada"})
        
        else:
            return render(request, "familia/inicio.html",{"mensaje":"Error"})

    else:  
        miFormulario= ObraFormulario()
        return render(request, "familia/obraFormulario.html",{"formulario":miFormulario})         




def artistaFormulario(request):
    if request.method=="POST":
        form = ArtistaFormulario(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            print(info)
            nombre=info.get("nombre")
            apellido=info.get("apellido")
            estilo=info.get("estilo")
            obras= info.get("obras")
            artista1= Artista(nombre=nombre,apellido=apellido,estilo=estilo,obras = obras)
            artista1.save()
            return render(request, "familia/inicio.html",{"mensaje":"Artista creado"})
        
        else:
            return render(request, "familia/inicio.html",{"mensaje":"Error"})

    else:  
        form = ArtistaFormulario()
        return render(request, "familia/artist-form.html",{"form":form})         




def busquedaNombre(request):
    return render(request,"familia/busquedaNombre.html")



def buscar(request):
    if request.GET["nombre"]:
        nombre= request.GET.get("nombre")  #(filter trae una lista, get me trae uno, all me trae todos en una lista)
        artistas= Artista.objects.filter(nombre= nombre)
        if len(artistas) != 0:
            return render(request, 'familia/ResultBusqueda.html', {"artistas":artistas})
        else:
            return render(request, 'familia/busquedaNombre.html', {"mensaje":"No hay artistas"})
    else:
        return render(request, 'familia/busquedaNombre.html', {"mensaje":"No ingresaste datos en la busqueda!"})
