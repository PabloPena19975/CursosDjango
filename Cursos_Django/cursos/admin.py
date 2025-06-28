from django.contrib import admin
from .models import Cursos
# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'costo', 'duracion', 'modalidad', 'activo')
    search_fields = ('nombre', 'modalidad')
    date_hierarchy = 'created'
    list_filter = ('costo', 'duracion', 'modalidad')
admin.site.register(Cursos, AdministrarModelo)