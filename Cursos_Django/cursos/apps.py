from django.apps import AppConfig


class CursosConfig(AppConfig):
    verbose_name='Convocatorias'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cursos'

    def ready(self):
        from django.contrib.admin.sites import AdminSite
        AdminSite.css = {
            'all': ('css/admin.css',),
        }
