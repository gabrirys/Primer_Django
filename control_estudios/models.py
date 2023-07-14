from django.db import models

# Create your models here.
from django.db import models

class Curso(models.Model):
    #los atributos de la clase son columnas de la tabla
    nombre = models.CharField(max_length=64) # funcion generar campo con texto con límite
    comision = models.IntegerField() # función para generar campo con números
    
class Estudiante(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True) # función para generar campo con fechas
    
    
class Profesor(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True)
    profesion = models.CharField(max_length=128)
    bio = models.TextField(blank=True) # funcion generar campo con texto sin límite
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_entrega = models.DateTimeField(auto_now_add=True)
    esta_aprobado = models.BooleanField(default=False)

    
    