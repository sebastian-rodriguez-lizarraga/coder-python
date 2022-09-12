from django.urls import path
from .views import *

urlpatterns=[
    path('',inicio,name='inicio'), #el path vacio '' para la pagina de inicio
    path('obrasDeArte/',obras_de_arte, name='obras_de_arte'),
    path('artistas/',artistaas, name='artistas'),
    path('obraFormulario/', obraFormulario, name='obraFormulario'),
    path('artistaFormulario/', artistaFormulario, name='artistaFormulario'),
    path('buscarArtista/', busquedaNombre, name='busquedaNombre'),
    path('buscar/',buscar,name='buscar'),
]


