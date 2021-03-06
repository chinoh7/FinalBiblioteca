from django.db import models
from django.contrib import admin
from django.utils import timezone
import os

# Create your models here.

class Autor(models.Model):
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    telefono = models.CharField(max_length=15)
    def __str__(self):
        return self.nombres

class Usuario(models.Model):
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    dpi = models.CharField(max_length=15)
    def __str__(self):
        return self.nombres

class Editorial(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40)
    telefono = models.CharField(max_length=15)
    def __str__(self):
        return self.nombre

class Pais(models.Model):
    nombre = models.CharField(max_length=40)
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo  =   models.CharField(max_length=30)
    #portada = models.CharField(max_length=15)
    #fotografia = models.ImageField(upload_to = '')
    fecha_publicacion = models.DateField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editoria = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo

class InfoLibro(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editoria = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

class Prestamos(models.Model):
    comentario = models.CharField(max_length=30)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolución = models.DateField()
    def __str__(self):
        return self.comentario

#---------------------------------------------------------
class InfoLibroInLine(admin.TabularInline):
    model = InfoLibro
    extra = 1

class AutorAdmin(admin.ModelAdmin):
    inlines = (InfoLibroInLine,)

class LibroAdmin(admin.ModelAdmin):
    inlines = (InfoLibroInLine,)

class Editorialdmin (admin.ModelAdmin):
    inlines = (InfoLibroInLine,)

class PaisAdmin (admin.ModelAdmin):
    inlines = (InfoLibroInLine,)

#---------------------------------------------------
class PrestamosInLine(admin.TabularInline):
    model = Prestamos
    extra = 1

class LibroAdmin (admin.ModelAdmin):
    inlines = (PrestamosInLine,)

class UsuarioAdmin (admin.ModelAdmin):
    inlines = (PrestamosInLine,)

#--------------------------------------

class Postear(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(
                    default=timezone.now)
    fecha_publicacion = models.DateTimeField(
                        blank=True, null=True)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
