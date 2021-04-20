from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos

# Create your views here.

# VISTA DEL BUSCADOR
def busqueda_productos(request):
    return render(request, "buscar_producto.html")

# VISTA DEL RESULTADO + CONTROL DE BÚSQUEDA STRING VACÍO
def resultado_busqueda(request):
    
    if request.GET["prd"]:
        # mensaje = "Artículo buscado: %r" % request.GET["prd"]

        producto = request.GET["prd"]

        articulos = Articulos.objects.filter(nombre__icontains = producto)

        return render(request, "resultado_busqueda.html", {"arts": articulos, "consulta": producto})

    else:
        mensaje = "No has escrito nada."
    return HttpResponse(mensaje)
