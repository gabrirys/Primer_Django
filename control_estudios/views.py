from django.shortcuts import render, redirect
from control_estudios.models import Curso, Estudiante
from control_estudios.forms import CursoFormulario
from django.urls import reverse, reverse_lazy

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView #IMPORTAR PARA LISTAS BASADAS EN CLASE
from django.contrib.auth.mixins import LoginRequiredMixin #
from django.contrib.auth.decorators import login_required #PARA PERMISOS DE USUARIOS


#def listar_estudiantes(request):
#    contexto = {
#            "estudiantes": Estudiante.objects.all(),
#    }
#    http_response = render(
#        request=request,
#        template_name="control_estudios/lista_estudiantes.html",
#        context=contexto,
#        )
#    return http_response
    
    
# VISTAS DE CURSOS (VISTAS BASADAS EN FUNCIONES)  

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
@login_required  
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
@login_required
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
@login_required
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


#VISTAS DE ESTUDIANTES (VISTAS BASADAS EN CLASES)

class EstudianteListView(LoginRequiredMixin, ListView):
    model = Estudiante
    template_name = 'control_estudios/lista_estudiantes.html'
    
class EstudianteCreateView(LoginRequiredMixin, CreateView):
    model = Estudiante
    fields = ('apellido', 'nombre', 'email', 'dni')
    success_url = reverse_lazy('lista_estudiantes')


class EstudianteDetailView(LoginRequiredMixin, DetailView):
    model = Estudiante
    success_url = reverse_lazy('lista_estudiantes')


class EstudianteUpdateView(LoginRequiredMixin, UpdateView):
    model = Estudiante
    fields = ('apellido', 'nombre', 'email', 'dni')
    success_url = reverse_lazy('lista_estudiantes')


class EstudianteDeleteView(LoginRequiredMixin, DeleteView):
    model = Estudiante
    success_url = reverse_lazy('lista_estudiantes')