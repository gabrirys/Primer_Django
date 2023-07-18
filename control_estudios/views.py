from django.shortcuts import render

# Create your views here.
def listar_estudiantes(request):
    contexto = {
            "estudiantes": [
                {"nombre": "Emanuel", "apellido": "Dautel", "nota": 7},
                {"nombre": "Manuela", "apellido": "Gomez", "nota": 10},
                {"nombre": "Ivan", "apellido": "Tomasevich", "nota": 4},
                {"nombre": "Carlos", "apellido": "Perez", "nota": 6},
            ]
    }
    http_response = render(
        request=request,
        template_name="control_estudios/lista_estudiantes.html",
        context=contexto,
        )
    return http_response
    
def listar_cursos(request):
    contexto = {
            "cursos": [
                {"nombre": "Física" , "comision": 1000},
                {"nombre": "Python", "comision": 55350},
                {"nombre": "Redes Sociales", "comision": 2000},
            ]
    }
    http_response = render(
        request=request,
        template_name="control_estudios/lista_cursos.html",
        context=contexto,
        )
    return http_response