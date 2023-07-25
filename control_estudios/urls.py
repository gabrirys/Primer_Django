#URLS ESPECÍFICAS DE LA APP

from django.contrib import admin
from django.urls import path

from control_estudios.views import (listar_estudiantes,
listar_cursos, 
crear_curso,
buscar_cursos,
)
#hay que importar la funciones desde el archvio donde esta generada

urlpatterns = [
    path("estudiantes/", listar_estudiantes, name="lista_estudiantes"),
    path("cursos/", listar_cursos, name="lista_cursos"),
    path("crear_curso/", crear_curso, name="crear_curso"),
    path("buscar-cursos/", buscar_cursos, name="buscar_cursos"),
]