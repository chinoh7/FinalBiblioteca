from django.contrib import admin
from biblioteca.models import Libro, LibroAdmin, Autor, AutorAdmin, Usuario,UsuarioAdmin, Editorial, Editorialdmin, Pais, PaisAdmin


admin.site.register(Libro, LibroAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Editorial, Editorialdmin)
admin.site.register(Pais, PaisAdmin)
admin.site.register(Usuario, UsuarioAdmin)
