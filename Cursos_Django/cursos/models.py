from django.db import models
from ckeditor.fields import RichTextField

class Cursos(models.Model): #Define la estructura de nuestra tabla
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    nombre= models.TextField(verbose_name="Nombre") #Texto largo
    duracion = models.CharField(max_length=50, verbose_name="Tiempo del curso")
    costo = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio")
    modalidad = models.CharField(max_length=20, verbose_name="Modalidad", choices=[
        ('presencial', 'Presencial'),
        ('en_linea', 'En línea'),
        ('hibrido', 'Híbrido'),
    ])
    activo = models.BooleanField(default=False, verbose_name="Activo")
    imagen = models.ImageField(null=True, upload_to="static", verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado") #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["created"]

    def __str__(self):
        return self.nombre
    
class Actividad (models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    curso = models.ForeignKey(Cursos,
            on_delete=models.CASCADE,verbose_name="Cursos")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    actividad = RichTextField(verbose_name="Actividad")

    class Meta:
        verbose_name= "Actividad"
        verbose_name_plural = "Actividad"
        ordering = ["-created"]

    def __str__(self):
        return str(self.curso)