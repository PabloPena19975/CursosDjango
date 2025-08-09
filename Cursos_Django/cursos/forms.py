from django import forms
from .models import Cursos
from django.forms import ModelForm

class CursosForm(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ['nombre', 'duracion', 'costo', 'modalidad', 'activo', 'imagen']