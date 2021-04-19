from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# VISTA DEL BUSCADOR
def busqueda_productos(request):
    return render(request, "buscar_producto.html")

# VISTA DEL RESULTADO
def resultado_busqueda(request):
    mensaje = "Artículo buscado: %r" %request.GET["prd"]

    return HttpResponse(mensaje)
