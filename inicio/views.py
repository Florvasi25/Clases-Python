from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from inicio.models import Perro
from django.shortcuts import render

#v1
# def inicio(request):
#     return HttpResponse('Hola Hola Hola')

#v2
# def inicio(request):
#     archivo = open(r'C:\Users\florv\Documents\CODERHOUSE\PYTHON\CLASES\proyectoFinalPython\proyectoFinalPython\templates\inicio.html', 'r')
#     template = Template(archivo.read())
#     archivo.close()
#     segundos = datetime.now().second
#     diccionario = {
#         'mensaje': 'Este es el mensaje de inicio...',
#         'segundos': segundos,
#         'segundo_par': segundos%2 == 0,
#         'segundo_redondo': segundos%10 == 0,
#         'listado_de_numeros': list(range(25)),
#     }
#     contexto = Context(diccionario)
#     renderizar_template = template.render(contexto)
#     return HttpResponse(renderizar_template)

#v3
# def inicio(request):
#     template = loader.get_template('inicio.html')

#     segundos = datetime.now().second
#     diccionario = {
#         'mensaje': 'Este es el mensaje de inicio...',
#         'segundos': segundos,
#         'segundo_par': segundos%2 == 0,
#         'segundo_redondo': segundos%10 == 0,
#         'listado_de_numeros': list(range(25)),
#     }

#     renderizar_template = template.render(diccionario)
#     return HttpResponse(renderizar_template)

#v4
def prueba(request):
    segundos = datetime.now().second
    diccionario = {
        'mensaje': 'Este es el mensaje de inicio...',
        'segundos': segundos,
        'segundo_par': segundos%2 == 0,
        'segundo_redondo': segundos%10 == 0,
        'listado_de_numeros': list(range(25)),
    }

    return render(request, 'inicio/prueba.html', diccionario)


def segunda_vista(request):
    return HttpResponse('<h1>Soy la segunda vista</h1>')

#v1
# def crear_perro(request, nombre, edad):
#     template = loader.get_template('crear_perro.html')
    
#     #V1
#     # diccionario = {
#     #     'nombre': nombre,
#     #     'edad': edad
#     # }

#     #V2
#     perro = Perro(nombre=nombre, edad=edad)
#     perro.save()
#     diccionario = {
#         'perro': perro
#     }

#     renderizar_template = template.render(diccionario)
#     return HttpResponse(renderizar_template)

#v2
def crear_perro(request, nombre, edad):
    perro = Perro(nombre=nombre, edad=edad)
    perro.save()
    diccionario = {
        'perro': perro
    }
    return render(request, 'inicio/crear_perro.html', diccionario)

def inicio(request):
    return render(request, 'inicio/inicio.html')