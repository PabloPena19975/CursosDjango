from django.contrib import admin
from .models import Cursos
from .models import Actividad
# Register your models here.





class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'costo', 'duracion', 'modalidad', 'activo')
    search_fields = ('nombre', 'modalidad')
    date_hierarchy = 'created'
    list_filter = ('costo', 'duracion', 'modalidad')
admin.site.register(Cursos, AdministrarModelo)

class AdministrarActividades(admin.ModelAdmin):
    list_display = ('id', 'actividad', 'curso', 'created')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
admin.site.register(Actividad, AdministrarActividades)


admin.site.site_header = "Administración de Cursos"
admin.site.site_title = "Panel de Control"
admin.site.index_title = "Gestión de Cursos Django"
