#URLS ESPECÍFICAS DE LA APP

from django.contrib import admin
from django.urls import path

from control_estudios.views import listar_estudiantes, listar_cursos
#hay que importar la funciones desde el archvio donde esta generada

urlpatterns = [
    path("estudiantes/", listar_estudiantes),
    path("cursos/", listar_cursos),
]