from django.contrib import admin
from .models import Categoria, Receta


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)


@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo',
        'categoria',
        'autor',
        'fecha_creacion'
    )

    list_filter = ('categoria', 'fecha_creacion')
    search_fields = ('titulo', 'descripcion')
