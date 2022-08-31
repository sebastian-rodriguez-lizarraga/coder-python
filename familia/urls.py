from django.urls import path
from .views import *

urlpatterns=[
    path('',inicio,name='inicio'), #el path vacio '' para la pagina de inicio
    path('obrasDeArte/',obras_de_arte, name='obras_de_arte'),
    path('artistas/',artistas, name='artistas'),
]


