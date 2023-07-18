"""
URL configuration for sistema_coder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from sistema_coder.views import saludar, saludar_hoy, saludar_html, listar_estudiantes
#hay que importar la funciones desde el archvio donde esta generada

urlpatterns = [
    path('admin/', admin.site.urls),
    path("saludo/", saludar), #agregamos la ruta
    path("fecha_hoy/", saludar_hoy),
    path("saludar_html/", saludar_html),
    path("bienvenidos_alumnos/", listar_estudiantes),
]