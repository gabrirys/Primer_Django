from django.contrib import admin

# Register your models here.
from control_estudios.models import Curso, Estudiante, Profesor, Entregable

admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)