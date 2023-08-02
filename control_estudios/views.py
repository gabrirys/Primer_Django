from django.shortcuts import render, redirect
from control_estudios.models import Curso, Estudiante
from control_estudios.forms import CursoFormulario
from django.urls import reverse

from django.contrib.auth.decorators import login_required

# Create your views here.
def listar_estudiantes(request):
    contexto = {
            "estudiantes": Estudiante.objects.all(),
    }
    http_response = render(
        request=request,
        template_name="control_estudios/lista_estudiantes.html",
        context=contexto,
        )
    return http_response
    
    
@login_required   
def listar_cursos(request):
    contexto = {
            "cursos": Curso.objects.all(),
            }
    http_response = render(
        request=request,
        template_name="control_estudios/lista_cursos.html",
        context=contexto,
        )
    return http_response
    
    
#CREACIÓN DE FORMULARIO
def crear_curso(request):
   if request.method == "POST":
   #Creo un objeto formulario con la data que envió el usuario
       formulario = CursoFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data["nombre"]
           comision = data["comision"]
           creador = request.user # Agregar el atributo del creador
           curso = Curso(nombre=nombre, comision=comision, creador=creador)
           curso.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('lista_cursos')  # estudios/cursos/
           return redirect(url_exitosa)
   else:  # GET
       formulario = CursoFormulario()
   http_response = render(
       request=request,
       template_name='control_estudios/formulario_curso.html',
       context={'formulario': formulario}
   )
   return http_response
   
#CREACIÓN DE BUSCADOR
def buscar_cursos(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        cursos = Curso.objects.filter(comision__contains=busqueda)
        # Ejemplo filtro avanzado
        # cursos = Curso.objects.filter(
        #     Q(nombre=busqueda) | Q(comision__contains=busqueda)
        # )
        contexto = {
            "cursos": cursos,
        }
        http_response = render(
            request=request,
            template_name='control_estudios/lista_cursos.html',
            context=contexto,
        )
        return http_response
        
#ELIMINAR CURSO       
def eliminar_curso(request, id):
    #obtienes el curso por meddio de su id
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
    #borra el curso de la base de datos
        curso.delete()
        #se reedirecciona a la url exsitosa
        url_exitosa = reverse('lista_cursos')
        return redirect(url_exitosa)
        

#EDITAR CURSOS
def editar_curso(request, id):
   curso = Curso.objects.get(id=id)
   if request.method == "POST":
       formulario = CursoFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           curso.nombre = data['nombre']
           curso.comision = data['comision']
           curso.save()
           url_exitosa = reverse('lista_cursos')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': curso.nombre,
           'comision': curso.comision,
       }
       formulario = CursoFormulario(initial=inicial)
   return render(
       request=request,
       template_name='control_estudios/formulario_curso.html',
       context={'formulario': formulario},
   )
