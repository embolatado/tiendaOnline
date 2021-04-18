from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos

# CREAR VISTAS PERSONALIZADAS PARA EL PANEL DE ADMINISTRACIÓN.
class panelClientes(admin.ModelAdmin):
    list_display=('nombre', 'email', 'tfno')
    search_fields = ("nombre", "tfno")

class panelArticulos(admin.ModelAdmin):
    list_filter=('seccion', )

# FILTRO FECHA
class panelPedidos(admin.ModelAdmin):
    list_display=("numero", "fecha")
    list_filter=("fecha",)
    date_hierarchy="fecha"

# Register your models here Y LAS VISTAS PERSONALIZADAS DEL /ADMIN
admin.site.register(Clientes, panelClientes)
admin.site.register(Articulos, panelArticulos)
admin.site.register(Pedidos, panelPedidos)
