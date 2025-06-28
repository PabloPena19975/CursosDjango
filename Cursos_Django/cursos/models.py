from django.db import models

class Cursos(models.Model): #Define la estructura de nuestra tabla

    nombre= models.TextField(verbose_name="Nombre") #Texto largo
    descripcion = models.TextField(verbose_name="Descripción")
    duracion = models.CharField(max_length=50, verbose_name="Tiempo del curso")
    costo = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio")
    modalidad = models.CharField(max_length=20, verbose_name="Modalidad", choices=[
        ('presencial', 'Presencial'),
        ('en_linea', 'En línea'),
        ('hibrido', 'Híbrido'),
    ])
    activo = models.BooleanField(default=False, verbose_name="Activo")
    imagen = models.ImageField(null=True, upload_to="fots", verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["created"]

    def __str__(self):
        return self.nombre