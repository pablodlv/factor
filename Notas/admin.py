from django.contrib import admin
from .models import Nota, Blog, Categoria, Autor, Etiqueta

# Register your models here.

admin.site.register(Blog)
admin.site.register(Nota)
admin.site.register(Categoria)
admin.site.register(Etiqueta)
admin.site.register(Autor)