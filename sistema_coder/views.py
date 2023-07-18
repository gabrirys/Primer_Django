from django.http import HttpResponse
#importamos los elementos Response para ver en la web

from datetime import datetime
from django.shortcuts import render

def saludar(request): 
#función que recibe una solicitud (request) http y retorna una respuesta http
    saludo = "Hola querido Gabriel"
    pagina_html = HttpResponse(saludo)
    return pagina_html
    
def saludar_hoy(request):
#función con parametro dinámicos
    dia = datetime.now()
    saludo = f"Hoy es {dia.day}/{dia.month}"
    pagina_html = HttpResponse(saludo)
    return pagina_html
    
def saludar_html(request):
    httpResponse = render(
        request=request,
        template_name="base.html",
        context={}
        )
    return httpResponse
    
    
def listar_estudiantes(request):
    contexto = {
            "estudiantes": [
                {"nombre": "Emanuel", "apellido": "Dautel"},
                {"nombre": "Manuela", "apellido": "Gomez"},
                {"nombre": "Ivan", "apellido": "Tomasevich"},
                {"nombre": "Carlos", "apellido": "Perez"},
            ]
    }
    http_response = render(
        request=request,
        template_name='base.html',
        context=contexto,
        )
    return http_response