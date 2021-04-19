from django.shortcuts import render

# Create your views here.

def busqueda_productos(request):
    return render(request, "buscar_producto.html")
