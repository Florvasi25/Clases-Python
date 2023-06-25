from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime

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
def inicio(request):
    template = loader.get_template('inicio.html')

    segundos = datetime.now().second
    diccionario = {
        'mensaje': 'Este es el mensaje de inicio...',
        'segundos': segundos,
        'segundo_par': segundos%2 == 0,
        'segundo_redondo': segundos%10 == 0,
        'listado_de_numeros': list(range(25)),
    }

    renderizar_template = template.render(diccionario)
    return HttpResponse(renderizar_template)


def segunda_vista(request):
    return HttpResponse('<h1>Soy la segunda vista</h1>')