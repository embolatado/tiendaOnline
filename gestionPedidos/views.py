from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

# VISTA DEL BUSCADOR
def busqueda_productos(request):
    return render(request, "buscar_producto.html")

# VISTA DEL RESULTADO + CONTROL DE BÚSQUEDA STRING VACÍO
def resultado_busqueda(request):
    if request.GET["prd"]:
        # mensaje = "Artículo buscado: %r" % request.GET["prd"]
        
        producto = request.GET["prd"]
        
        # LIMITAR NÚMERO CARACTERES QUE SE ENVÍAN AL SERVIDOR
        if len(producto) > 30:
            mensaje = "Texto de búsqueda demasiado largo."

        else:
            articulos = Articulos.objects.filter(nombre__icontains = producto)

            return render(request, "resultado_busqueda.html", {"arts": articulos, "consulta": producto})

    else:
        mensaje = "No has escrito nada."
    
    return HttpResponse(mensaje)


def form_contacto(request):

    if request.method == 'POST':

        # CREACIÓN VARIABLES PARA Forms
        betreff = request.POST['asunto']
        nachricht = request.POST['mensajecntc'] + " " + request.POST['emailcntc']

        email_desde = settings.EMAIL_HOST_USER
        email_para = ['shhittybikes@gmail.com']
        send_mail(betreff, nachricht, email_desde, email_para)
    
        return render(request, "gracias.html")
    
    return render(request, "contactenos.html")


def test_plantillas(request):
    
    return render(request, 'prueba_plantillas.html')
