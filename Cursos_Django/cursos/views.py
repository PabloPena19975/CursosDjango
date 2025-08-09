from django.shortcuts import render
from cursos.forms import CursosForm
from .models import Cursos
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.
def principal(request):

    return render(request,"cursos/principal.html")

def cursosConsulta(request):
    curso = Cursos.objects.all()
    return render(request, 'cursos/cursos.html', {'cursos': curso})


def registrar(request):
    cursos = Cursos.objects.all()

    if request.method == 'POST':
        form = CursosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = CursosForm()  # Limpiar el formulario tras guardar
            return render(request, 'cursos/cursos.html', {
                'form': form,
                'exito': True,
                'cursos': cursos
            })

    else:
        form = CursosForm()

    return render(request, 'cursos/cursosNuevos.html', {
        'form': form,
        'cursos': cursos
    })


def eliminarCurso( request, id,
        confirmacion='cursos/confirmarEliminacion.html'):
        curso = get_object_or_404(Cursos, id=id)
        if request.method=='POST':
            curso.delete()
            curso=Cursos.objects.all()
            return render(request,"cursos/cursos.html", {'cursos':curso})
        return render(request, confirmacion, {'object':curso})

def consultarCursoIndividual(request, id):
    curso=Cursos.objects.get(id=id)
    #get permite establecer una condicionante a la consulta y recupera el objetos
    #del modelo que cumple la condición ( registro de la tabla ComentariosContacto.)
    #get se emplea cuando se sabe que solo hay un objeto que coincide con su
    #consulta

    return render(request,"cursos/formEditarCursos.html",{'curso':curso})
    #Indicamos el lugar donde se renderizará el resultado de esta vista
    # y enviamos la lista de alumnos recuperacos


def editarCurso(request, id):
    curso = get_object_or_404(Cursos, id=id)
    form = CursosForm(request.POST, instance=curso)
    #Referenciamos que el elemento del formulario pertenece al comentario
    # ya existente
    if form.is_valid():
        form.save() #si el registro ya existe, se modifica.
        curso=Cursos.objects.all()
        return render(request,"cursos/cursos.html",{'cursos':curso})
    #Si el formulario no es valido nos regresa al formulario para verificar
    #datos
    return render(request,"cursos/formEditarCursos.html",{'cursos':curso})