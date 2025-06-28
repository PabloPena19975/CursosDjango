from django.shortcuts import render, HttpResponse

# Create your views here.

menu = """
        <a href="/">Home</a> |
        <a href="/cursos">Cursos</a> |
        <a href="/contacto">Contactanos</a>
        <hr>
    """

def principal(request):
    
    contenido = """
    <style>
        body { font-family: Arial; background-color: #f0f0f0; padding: 20px; }
        h1 { color: darkblue; }
        a { margin-right: 15px; text-decoration: none; color: darkgreen; }
    </style>
    <h1>Bienvenido a esta página, aquí mostraremos mi trabajo sobre Django</h1>
    """

    return HttpResponse(menu + contenido)


def cursos(reques):
    contenido="""<h2> Cursos </h2>
    <p>Cursos:
        <select> name="cusos">
            <option>Base de Datos.</option>
            <option>Programación.</option>
        </select>
    </p>
    """

    return HttpResponse(contenido)


def contacto(request):
    contenido="""<h2>Contacto</h2>
    <p>Nombre:<input type="text" name="nombre"></p>
    <p>Correo: <input type="text" name="correo"</p>
    
        <p>Cursos:
        <select> name="cusos">
            <option>Base de Datos.</option>
            <option>Programación.</option>
        </select>
        </p>
    <p>Comentario:</p><p><textarea cols="50" rows="10"></textarea></p>

    <p><input type="Button" name="enviar" value="Enviar"/></p>
    """
    return HttpResponse(contenido)